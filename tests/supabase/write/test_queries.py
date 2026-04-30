from src.models.followup import FollowupModel
from src.db.queries.write import save_followup

# These are my account's test user and contact IDs, replace with your own for testing
TEST_USER_ID     = "1d33b810-7e13-4d0d-b9fd-8da8bae3ac14"
TEST_CONTACT_ID  = "5582d451-d476-4655-9462-998b6e9ecc86"

def test_save_followup_query():
    print("\n───────────────────────────────────── Save Followup Query ─────────────────────────────────────")
    followup = FollowupModel(
        user_id=TEST_USER_ID,
        contact_id=TEST_CONTACT_ID,
        status="draft",
        
        draft_message="Hello, how are you doing?",
        scheduled_for="2023-10-15T10:00:00Z",
        ai_reasoning="Based on previous interactions, this is a good time to check in."
    )
    save_followup(followup)
    print("✓ PASSED")


if __name__ == "__main__":
    print("Running DB query tests...")
    test_save_followup_query()
    print("\n✓ ALL TESTS HAVE PASSED")