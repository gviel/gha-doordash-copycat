def test_estimate_time_returns_status_200(client):
    response = client.get("/estimate-time/12.3")
    assert response.status_code == 200
    assert response.json()["estimated_delivery_time_minutes"] == 71.5