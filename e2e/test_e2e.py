import requests
import time

BASE_URL = "http://127.0.0.1:8080"

def wait_for_app():
    for _ in range(20):
        try:
            r = requests.get(f"{BASE_URL}/health", timeout=2)
            if r.status_code == 200:
                return
        except Exception:
            pass
        time.sleep(1)
    raise RuntimeError("Application non disponible")

def test_health_e2e():
    wait_for_app()
    r = requests.get(f"{BASE_URL}/health", timeout=2)
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_hello_e2e():
    r = requests.get(f"{BASE_URL}/hello", timeout=2)
    assert r.status_code == 200
    assert r.json() == {"message": "deployment ok"}