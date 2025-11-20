from database.config import SessionLocal, engine
from database.base import Base
from models.user import User
from utils.auth import get_password_hash

def fix_users():
    db = SessionLocal()
    try:
        # Видаляємо всіх існуючих користувачів
        db.query(User).delete()
        db.commit()
        print("🗑️ Старі користувачі видалені")
        
        # Створюємо нового користувача з правильним хешем
        hashed_password = get_password_hash("password123")
        user = User(
            email="test@example.com",
            username="testuser", 
            hashed_password=hashed_password
        )
        db.add(user)
        db.commit()
        
        print("✅ Новий користувач створений:")
        print(f"   Email: test@example.com")
        print(f"   Password: password123")
        print(f"   Хеш: {hashed_password[:30]}...")
        
    except Exception as e:
        print(f"❌ Помилка: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    fix_users()