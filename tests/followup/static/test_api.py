import requests, json

if __name__ == "__main__":   
    # Relevant context from database for generating followup message. 
    # In proper implementation, the backend would fetch this and create a context object from the DB based on user_id, contact_id, and note_id.

    user_ctx = json.dumps({
        # User's profile
        # "id": "a1b2c3d4-0001-0001-0001-000000000001",
        # "auth_id": "auth-uuid-0001",
        # "role": "user",
        # "email": "tio@example.com",
        "first_name": "Tio",
        "last_name": "Rivera",
        # "display_name": "Tio",
        "headline": "CS Student & Aspiring ML Engineer",
        "goals": ["Break into AI product roles", "Build ML portfolio"],
        # "meridian_credits": 100
        })  
    
    target_ctx = json.dumps({
        # Target's profile
        # "id": "b1b2c3d4-0002-0002-0002-000000000002",
        # "user_id": "a1b2c3d4-0001-0001-0001-000000000001",
        "name": "Sarah Chen",
        # "email": "sarah.chen@novamind.ai",
        # "phone": "+1-555-0102",
        "context": "AI Product Lead at NovaMind AI (Series B). Spoke at NeurIPS. Recently posted about challenges productizing LLMs. Met at AI Founders Meetup.",
        
        # Notes on target
        # "id": "c1b2c3d4-0003-0003-0003-000000000003",
        # "user_id": "a1b2c3d4-0001-0001-0001-000000000001",
        # "source_event_id": None,
        "title": "Untitled note",
        "text": "{\"ops\":[{\"insert\":\"Sarah mentioned NovaMind is hiring for PM roles in Q3. Bring up my LLM project next time. She likes founders who ship fast.\"}]}",
        "checklist": [
            { "text": "Send portfolio link", "done": False },
            { "text": "Reference NeurIPS talk", "done": False },
        ],
        # "reminder_at": "2025-05-01T09:00:00Z",
        # "needs_processing": False,
        # "processing_metadata": {},
        
        # Previous followups
        "followups": [{
            # "id": "d1b2c3d4-0004-0004-0004-000000000004",
            # "user_id": "a1b2c3d4-0001-0001-0001-000000000001",
            # "contact_id": "b1b2c3d4-0002-0002-0002-000000000002",
            "status": "draft",
            "message": "Hey Sarah, loved your NeurIPS talk on LLM productization — I've been building something in that space and would love to get your take on it.",
            "scheduled_for": "2025-05-01T09:00:00Z",
        },
        {
            # "id": "e1b2c3d4-0005-0005-0005-000000000005",
            # "user_id": "a1b2c3d4-0001-0001-0001-000000000001",
            # "contact_id": "b1b2c3d4-0002-0002-0002-000000000002",
            # "note_id": "c1b2c3d4-0003-0003-0003-000000000003",
            "status": "sent",
            "message": "Following up on my previous message — would love to connect and get your insights on AI product roles at NovaMind!",
            "scheduled_for": "2025-05-08T09:00:00Z",
        }]
    })
                            
    r = requests.get("http://localhost:8000/followup/test/generate", params={
        "user_context": user_ctx,
        "target_context": target_ctx
    })

    print(r.status_code)
    print(r.text)
    print(r.json())