from app import app

client = app.test_client()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {
        "status": "healthy",
        "application": "student-ml-api",
        "version": "wrong",
    }


def test_predict_success():
    response = client.post("/predict", json={"value": 10})
    assert response.status_code == 200
    assert response.get_json() == {"input": 10, "prediction": 20}


def test_predict_missing_input():
    response = client.post("/predict", json={})
    assert response.status_code == 400
    assert "value" in response.get_json()["error"]


def test_predict_invalid_input():
    response = client.post("/predict", json={"value": "ten"})
    assert response.status_code == 400
    assert response.get_json()["error"] == "value must be a number"
