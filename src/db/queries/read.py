from .. import supabase

def users_table_query(user_id: str) -> dict:
    result = supabase.table("users").select("*").eq("id", user_id).execute()
    if result.data:
        user = result.data[0]
        return {
            "first_name": user.get("first_name"),
            "last_name": user.get("last_name"),
            "headline": user.get("headline"),
            "goals": user.get("goals")
        }
    return {}

def contacts_table_query(contact_id: str) -> dict:
    result = supabase.table("contacts").select("*").eq("id", contact_id).execute()
    if result.data:
        contact = result.data[0]
        return {
            "name": contact.get("name"),
            "context": contact.get("context")
        }
    return {}

def enriched_table_query(contact_id: str) -> dict:
    result = supabase.table("enrichment_caches").select("*").eq("contact_id", contact_id).eq("status", "completed").execute()
    if result.data:
        return {"payload": result.data[0].get("payload")}
    return {}

def notes_from_entities_query(contact_id: str) -> list:
    note_ids = []

    # contact is entity_a, note is entity_b
    result_a = supabase.table("entity_links").select("*").eq("entity_a_id", contact_id).eq("entity_a_type", "contact").eq("entity_b_type", "note").execute()
    if result_a.data:
        for entity in result_a.data:
            note_ids.append(entity.get("entity_b_id"))

    # contact is entity_b, note is entity_a
    result_b = supabase.table("entity_links").select("*").eq("entity_b_id", contact_id).eq("entity_b_type", "contact").eq("entity_a_type", "note").execute()
    if result_b.data:
        for entity in result_b.data:
            note_ids.append(entity.get("entity_a_id"))

    return note_ids

def notes_table_query(note_ids: list) -> list:
    if not note_ids:
        return []
    result = supabase.table("notes").select("*").in_("id", note_ids).execute()
    if result.data:
        return [
            {
                "title": note.get("title"),
                "text": note.get("text"),
                "checklist": note.get("checklist")
            }
            for note in result.data
        ]
    return []

def followups_table_query(user_id: str, contact_id: str) -> list:
    result = supabase.table("follow_ups").select("*").eq("user_id", user_id).eq("contact_id", contact_id).execute()
    if result.data:
        return [
            {
                "status": f.get("status"),
                "draft_message": f.get("draft_message"),
                "scheduled_for": f.get("scheduled_for")
            }
            for f in result.data
        ]
    return []

def get_followup_contexts(user_id: str, contact_id: str) -> tuple:
    user_context = users_table_query(user_id)
    target_context = {}

    note_ids = notes_from_entities_query(contact_id)
    target_context.update(contacts_table_query(contact_id))
    target_context["enriched_data"] = enriched_table_query(contact_id)
    target_context["all_relevant_notes"] = notes_table_query(note_ids)
    target_context["previous_followups"] = followups_table_query(user_id, contact_id)

    return user_context, target_context