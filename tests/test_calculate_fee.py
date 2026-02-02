def test_calculate_fee_valid_payload(client):
    payload = {
        "distance_km": 10.5,
        "weight_kg": 2.0,
    }
    response = client.post("/calculate-fee/", json=payload)
    #TODO tester la valeur de réponse
    assert response.status_code == 200
    assert "delivery_fee" in  response.json()
    assert response.json()["delivery_fee"] == 22.75