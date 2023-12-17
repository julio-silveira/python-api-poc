import pathlib
import os

from typing import Optional

from dotenv import load_dotenv

ROOT = pathlib.Path(__file__).resolve().parent
load_dotenv()


class Settings:
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.getenv("DATABASE_URL")

    class Config:
        case_sensitive = True


settings = Settings()
