# test_api.py
import requests

def test_example():
    response = requests.get("https://api.github.com")
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert "application/json" in response.headers["Content-Type"], "Expected JSON response"
    print("Test passed: API is reachable and returned valid JSON response.")
