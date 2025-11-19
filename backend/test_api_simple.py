import requests
import json

BASE_URL = "http://localhost:8000"

def test_api():
    print("=== Тест API ===")
    
    # Тест кореневого ендпоінта
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"✅ Головна сторінка: {response.json()}")
    except Exception as e:
        print(f"❌ Помилка головної сторінки: {e}")
        return
    
    # Тест реєстрації
    try:
        register_data = {
            "email": "apitest@example.com",
            "username": "apitestuser",
            "password": "testpass123"
        }
        response = requests.post(f"{BASE_URL}/auth/register", json=register_data)
        if response.status_code == 200:
            print(f"✅ Реєстрація успішна: {response.json()['username']}")
        else:
            print(f"❌ Помилка реєстрації: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Помилка реєстрації: {e}")
    
    # Тест логіну - ВИПРАВЛЕНО
    try:
        login_data = {
            "email": "apitest@example.com",
            "password": "testpass123"
        }
        # Використовуємо параметри URL замість JSON body
        response = requests.post(
            f"{BASE_URL}/auth/login", 
            params=login_data  # Змінено з json= на params=
        )
        if response.status_code == 200:
            token = response.json()["access_token"]
            print(f"✅ Логін успішний! Токен: {token[:50]}...")
        else:
            print(f"❌ Помилка логіну: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"❌ Помилка логіну: {e}")

if __name__ == "__main__":
    test_api()