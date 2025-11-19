import requests

def test_login():
    print("=== Тест логіну ===")
    
    # Спочатку зареєструємо користувача
    register_data = {
        "email": "debug@example.com",
        "username": "debuguser",
        "password": "debug123"
    }
    
    try:
        # Реєстрація
        response = requests.post("http://127.0.0.1:8000/auth/register", json=register_data)
        print(f"Реєстрація: {response.status_code} - {response.text}")
        
        # Логін
        login_data = {
            "email": "debug@example.com",
            "password": "debug123"
        }
        response = requests.post("http://127.0.0.1:8000/auth/login", json=login_data)
        print(f"Логін: {response.status_code} - {response.text}")
        
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    test_login()