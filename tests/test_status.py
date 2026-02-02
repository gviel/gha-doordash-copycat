def test_status_endpoint_ok(client):
    response = client.get("/status/")
    assert response.status_code == 200