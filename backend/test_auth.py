print("=== Тест авторизації ===")

try:
    from database.config import SessionLocal, engine
    from database.base import Base
    from models.user import User
    
    # Створюємо таблиці
    Base.metadata.create_all(bind=engine)
    
    db = SessionLocal()
    
    # Тест реєстрації
    from schemas.user import UserCreate
    from routers.auth import register
    
    test_user_data = UserCreate(
        email="test2@example.com",
        username="testuser2",
        password="testpassword123"
    )
    
    # Викликаємо функцію реєстрації
    from utils.auth import get_password_hash
    hashed_password = get_password_hash(test_user_data.password)
    
    new_user = User(
        email=test_user_data.email,
        username=test_user_data.username,
        hashed_password=hashed_password
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    print(f" Користувач створений: {new_user.username}")
    
    # Тест логіну
    from utils.auth import verify_password, create_access_token
    
    # Перевіряємо пароль
    user = db.query(User).filter(User.email == "test2@example.com").first()
    if user and verify_password("testpassword123", user.hashed_password):
        token = create_access_token(data={"sub": user.username})
        print(f" Логін успішний! Токен: {token[:50]}...")
    else:
        print(" Помилка логіну")
    
    db.close()
    
except Exception as e:
    print(f" Помилка: {e}")
    import traceback
    traceback.print_exc()

print("=== Тест завершено ===")