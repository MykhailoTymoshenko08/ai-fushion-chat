from database.config import SessionLocal
from models.user import User
from utils.auth import get_password_hash

def create_test_user():
    db = SessionLocal()
    try:
        # Перевіряємо чи вже існує
        existing = db.query(User).filter(User.email == "test@example.com").first()
        if existing:
            print("✅ Користувач вже існує")
            return
        
        # Створюємо нового користувача
        hashed_password = get_password_hash("password123")
        user = User(
            email="test@example.com",
            username="testuser",
            hashed_password=hashed_password
        )
        db.add(user)
        db.commit()
        print("✅ Тестовий користувач створений:")
        print(f"   Email: test@example.com")
        print(f"   Password: password123")
        
    except Exception as e:
        print(f"❌ Помилка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_test_user()