from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_warning_forwarded():
    response = client.post("/notify", json={
        "Type": "Warning",
        "Name": "Disk Failure",
        "Description": "Disk full"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "forwarded"

def test_info_ignored():
    response = client.post("/notify", json={
        "Type": "Info",
        "Name": "Daily Report",
        "Description": "Report generated"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "ignored"

