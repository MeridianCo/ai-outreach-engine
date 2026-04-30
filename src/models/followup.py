from enum import Enum
from pydantic import BaseModel

class FollowupStatus(str, Enum):
    DRAFT = "draft"
    SCHEDULED = "scheduled"
    SENT = "sent"
    SKIPPED = "skipped"

class FollowupModel(BaseModel):
    user_id: str
    contact_id: str
    status: FollowupStatus

    draft_message: str = None
    scheduled_for: str = None
    ai_reasoning: str = None
