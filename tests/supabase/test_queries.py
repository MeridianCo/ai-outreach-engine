import json
from db.queries.read import (
    users_table_query,
    contacts_table_query,
    enriched_table_query,
    notes_from_entities_query,
    notes_table_query,
    followups_table_query,
    followup_contexts_query
)

# These are my account's test user and contact IDs, replace with your own for testing
TEST_USER_ID     = "1d33b810-7e13-4d0d-b9fd-8da8bae3ac14"
TEST_CONTACT_ID  = "5582d451-d476-4655-9462-998b6e9ecc86"
TEST_NOTE_IDS    = ["963a562b-16e6-48f3-8dd6-7ce2d8ed50a2"]

def test_users_table_query():
    print("\n───────────────────────────────────── User Table Query ─────────────────────────────────────")
    result = users_table_query(TEST_USER_ID)
    print(json.dumps(result, indent=2, default=str))
    assert isinstance(result, dict), "Should return a dict"
    assert "first_name" in result
    assert "goals" in result
    print("✓ PASSED")

def test_contacts_table_query():
    print("\n───────────────────────────────────── Contacts Table Query ─────────────────────────────────────")
    result = contacts_table_query(TEST_CONTACT_ID)
    print(json.dumps(result, indent=2, default=str))
    assert isinstance(result, dict), "Should return a dict"
    assert "name" in result
    assert "context" in result
    print("✓ PASSED")

def test_enriched_table_query():
    print("\n───────────────────────────────────── Enriched Table Query ─────────────────────────────────────")
    result = enriched_table_query(TEST_CONTACT_ID)
    print(json.dumps(result, indent=2, default=str))
    assert isinstance(result, dict), "Should return a dict"
    # may be empty if no completed enrichment exists — that's fine
    print("✓ PASSED")

def test_notes_from_entities_query():
    print("\n───────────────────────────────────── Notes from Entities Query ─────────────────────────────────────")
    result = notes_from_entities_query(TEST_CONTACT_ID)
    print(json.dumps(result, indent=2, default=str))
    assert isinstance(result, list), "Should return a list"
    print(f"  found {len(result)} linked note id(s)")
    print("✓ PASSED")

def test_notes_table_query():
    print("\n───────────────────────────────────── Notes Table Query ─────────────────────────────────────")
    result = notes_table_query(TEST_NOTE_IDS)
    print(json.dumps(result, indent=2, default=str))
    assert isinstance(result, list), "Should return a list"
    if result:
        assert "title" in result[0]
        assert "text" in result[0]
        assert "checklist" in result[0]
    print("✓ PASSED")

def test_notes_table_query_empty():
    print("\n───────────────────────────────────── Notes Table Query (empty input) ─────────────────────────────────────")
    result = notes_table_query([])
    print(json.dumps(result, indent=2, default=str))
    assert result == [], "Should return empty list for empty input"
    print("✓ PASSED")

def test_followups_table_query():
    print("\n───────────────────────────────────── Followups Table Query ─────────────────────────────────────")
    result = followups_table_query(TEST_USER_ID, TEST_CONTACT_ID)
    print(json.dumps(result, indent=2, default=str))
    assert isinstance(result, list), "Should return a list"
    if result:
        assert "status" in result[0]
        assert "draft_message" in result[0]
        assert "scheduled_for" in result[0]
    print("✓ PASSED")

def test_followup_contexts_query():
    print("\n───────────────────────────────────── Followup Contexts Query ─────────────────────────────────────")
    user_ctx, target_ctx = followup_contexts_query(TEST_USER_ID, TEST_CONTACT_ID)
    print("user_context:")
    print(json.dumps(user_ctx, indent=2, default=str))
    print("target_context:")
    print(json.dumps(target_ctx, indent=2, default=str))
    assert isinstance(user_ctx, dict),   "user_context should be a dict"
    assert isinstance(target_ctx, dict), "target_context should be a dict"
    assert "name" in target_ctx
    assert "previous_followups" in target_ctx
    assert "all_relevant_notes" in target_ctx
    print("✓ PASSED")

if __name__ == "__main__":
    print("Running DB query tests...")
    test_users_table_query()
    test_contacts_table_query()
    test_enriched_table_query()
    test_notes_from_entities_query()
    test_notes_table_query()
    test_notes_table_query_empty()
    test_followups_table_query()
    test_followup_contexts_query()
    print("\n✓ ALL TESTS HAVE PASSED")