
from . import supabase

def user_data_query(user_id: str) -> str:
    user_table = supabase.table("users")
    user_data_raw = user_table.select("*").eq("id", user_id).execute()

    if user_data_raw.status_code == 200 and user_data_raw.data:
        user_data = user_data_raw.data[0]
        return {
            "name": user_data.get("name"),
            "email": user_data.get("email"),
            "job_title": user_data.get("job_title"),
            "company": user_data.get("company")
        }

def contact_data_query(contact_id: str) -> str:
    contacts_table = supabase.table("contacts")
    contact_data_raw = contacts_table.select("*").eq("id", contact_id).execute()

    if contact_data_raw.status_code == 200 and contact_data_raw.data:
        contact_data = contact_data_raw.data[0]
        return {
            "name": contact_data.get("name"),
            "email": contact_data.get("email"),
            "job_title": contact_data.get("job_title"),
            "company": contact_data.get("company")
        }

def followup_message_query(contact_id: str) -> str:
    user_context = None
    target_context = None
        
    contacts_table = supabase.table("contacts")
    user_id_raw = contacts_table.select("user_id").eq("id", contact_id).execute()

    if user_id_raw.status_code == 200 and user_id_raw.data:
        user_id = user_id_raw.data[0].get("user_id")
        if user_id:
            user_context = user_data_query(user_id)
    target_context = contact_data_query(contact_id)

    return user_context, target_context