
from . import supabase

def users_table_query(user_id: str) -> dict:
    user_table = supabase.table("users")
    user_data_raw = user_table.select("*").eq("id", user_id).execute()

    if user_data_raw.status_code == 200 and user_data_raw.data:
        user_data = user_data_raw.data[0]
        return {
            "first_name": user_data.get("first_name"),
            "last_name": user_data.get("last_name"),
            "headline": user_data.get("headline"),
            "goals": user_data.get("goals")
        }

def contacts_table_query(contact_id: str) -> dict:
    contacts_table = supabase.table("contacts")
    contact_data_raw = contacts_table.select("*").eq("id", contact_id).execute()

    if contact_data_raw.status_code == 200 and contact_data_raw.data:
        contact_data = contact_data_raw.data[0]
        return {
            "name": contact_data.get("name"),
            "context": contact_data.get("context")
        }
    
def enriched_table_query(contact_id: str) -> dict:
    enriched_table = supabase.table("enrichment_caches")
    enriched_data_raw = enriched_table.select("*").eq("contact_id", contact_id).eq("status", "completed").execute()

    if enriched_data_raw.status_code == 200 and enriched_data_raw.data:
        enriched_data = enriched_data_raw.data[0]
        return {
            "payload": enriched_data.get("payload")
        }
    
def notes_from_entities_query(contact_id: str) -> list:
    note_ids = []
    entities_table = supabase.table("entities")

    entities_a_raw = entities_table.select("*").eq("entity_a_id", contact_id).eq("entity_b_type", "note").execute()
    if entities_a_raw.status_code == 200 and entities_a_raw.data:
        for entity in entities_a_raw.data:
            note_ids.append(entity.get("entity_b_id"))

    entities_b_raw = entities_table.select("*").eq("entity_b_id", contact_id).eq("entity_a_type", "note").execute()
    if entities_b_raw.status_code == 200 and entities_b_raw.data:
        for entity in entities_b_raw.data:
            note_ids.append(entity.get("entity_a_id"))

    return note_ids
    
def notes_table_query(notes_ids: list) -> list:
    notes_data = []
    notes_table = supabase.table("notes")

    notes_data_raw = notes_table.select("*").in_("id", notes_ids).execute()
    if notes_data_raw.status_code == 200 and notes_data_raw.data:
        for note in notes_data_raw.data:
            notes_data.append({
                "title": note.get("title"),
                "text": note.get("text"),
                "checklist": note.get("checklist")
            })
    return notes_data
    
def followups_table_query(user_id: str, contact_id: str) -> list:
    followups_table = supabase.table("followups")
    followup_data_raw = followups_table.select("*").eq("user_id", user_id).eq("contact_id", contact_id).execute()

    if followup_data_raw.status_code == 200 and followup_data_raw.data:
        for followup in followup_data_raw.data:
            return {
                "status": followup.get("status"),
                "message": followup.get("message"),
                "scheduled_for": followup.get("scheduled_for")
            }

def followup_contexts_query(user_id: str, contact_id: str) -> tuple:
    user_context = users_table_query(user_id)

    target_context = {}
    notes_ids = notes_from_entities_query(contact_id)
    target_context.update(contacts_table_query(contact_id))
    target_context.update({"enriched_data": enriched_table_query(contact_id)})
    target_context.update({"all_relevant_notes": notes_table_query(notes_ids)})
    target_context.update({"previous_followups": followups_table_query(user_id, contact_id)})

    return user_context, target_context 