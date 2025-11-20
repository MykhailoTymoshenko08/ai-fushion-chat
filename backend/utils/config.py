import os
from dotenv import load_dotenv

# Завантажуємо змінні з .env файлу
load_dotenv()

class Settings:
    def __init__(self):
        self.database_url = os.getenv("DATABASE_URL", "sqlite:///./ai_fusion_chat.db")
        self.secret_key = os.getenv("SECRET_KEY", "your-secret-key-change-in-production-12345")
        self.algorithm = os.getenv("ALGORITHM", "HS256")
        self.access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
        
        # API keys
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "test-key")
        self.anthropic_api_key = os.getenv("ANTHROPIC_API_KEY", "test-key")
        self.google_api_key = os.getenv("GOOGLE_API_KEY", "test-key")
        self.mistral_api_key = os.getenv("MISTRAL_API_KEY", "test-key")

settings = Settings()