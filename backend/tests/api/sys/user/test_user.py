from fastapi.testclient import TestClient

BASE_URL = "/api/v1/sys/user"

def test_user_add(client: TestClient):
    user = {
        "email": "email@email.com",
        "username": "admin",
        "password": "admin123",
    }
    r = client.post(f"{BASE_URL}/add", json=user)
    r_json = r.json()
    print(r_json)
    assert r.status_code == 200
    assert r_json.get('success') == True
    assert r_json.get('code') == 200