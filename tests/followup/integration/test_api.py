import requests

# These are my account's test user and contact IDs, replace with your own for testing
TEST_USER_ID     = "1d33b810-7e13-4d0d-b9fd-8da8bae3ac14"
TEST_CONTACT_ID  = "5582d451-d476-4655-9462-998b6e9ecc86"

def test_generate_followup():
    r = requests.get(
        "http://localhost:8000/followup/generate",
        params={
            "user_id": TEST_USER_ID,
            "contact_id": TEST_CONTACT_ID,
        },
    )

    print(f"\nStatus: {r.status_code}")
    print(f"Response: {r.text}")

    assert r.status_code == 200
    data = r.json()
    print(f"JSON: {data}")
    assert data is not None