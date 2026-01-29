from fastapi.testclient import TestClient

BASE_URL = "/api/v1/snc/banner"

def test_banner_published(client: TestClient):
    r = client.get(f"{BASE_URL}/published")
    r_json = r.json()
    assert r.status_code == 200
    assert r_json.get('success') == True
    assert r_json.get('code') == 200

def test_banner_add(client: TestClient):
    banner = {
        "name": "name",
        "image_url": "url",
        "target_url": "target_url",
        "target_type": "target_type",
        "sort_order": 1,
        "status": "status",
    }
    r = client.post(f"{BASE_URL}/add", json=banner)
    r_json = r.json()
    print(r_json)
    assert r.status_code == 200
    assert r_json.get('success') == True
    assert r_json.get('code') == 200