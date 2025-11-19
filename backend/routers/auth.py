from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database.config import get_db
from models.user import User
from schemas.user import UserCreate, UserResponse, Token, UserLogin
from utils.auth import get_password_hash, verify_password, create_access_token
import traceback  # Додано

router = APIRouter()

@router.post("/login", response_model=Token)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    try:
        print(f"🔍 Спроба логіну для: {user_data.email}")
        
        # Шукаємо користувача по email
        user = db.query(User).filter(User.email == user_data.email).first()
        
        if not user:
            print("❌ Користувач не знайдений")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Невірний email або пароль",
            )
        
        print(f"🔍 Користувач знайдений: {user.username}")
        print(f"🔍 Хеш пароля в базі: {user.hashed_password[:20]}...")
        print(f"🔍 Перевіряємо пароль...")
        
        # Перевіряємо пароль
        password_valid = verify_password(user_data.password, user.hashed_password)
        print(f"🔍 Пароль валідний: {password_valid}")
        
        if not password_valid:
            print("❌ Невірний пароль")
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Невірний email або пароль",
            )
        
        # Створюємо токен
        access_token = create_access_token(data={"sub": user.username})
        print(f"✅ Успішний логін для: {user.username}")
        print(f"🔑 Токен створено: {access_token[:50]}...")
        
        return {
            "access_token": access_token,
            "token_type": "bearer"
        }
        
    except Exception as e:
        print(f"💥 КРИТИЧНА ПОМИЛКА в login:")
        print(f"Повідомлення: {e}")
        print(f"Траса:")
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail="Внутрішня помилка сервера"
        )