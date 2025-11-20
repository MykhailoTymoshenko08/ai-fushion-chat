from database.config import SessionLocal
from models.user import User

def check_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        print(f"📊 Кількість користувачів в базі: {len(users)}")
        for user in users:
            print(f"👤 {user.id}: {user.email} - {user.username}")
    except Exception as e:
        print(f"❌ Помилка: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    check_users()