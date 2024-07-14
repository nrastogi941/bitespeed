import os

if os.getenv("ENV") in ["DEV", "TEST"]:
    from dotenv import load_dotenv

    load_dotenv(os.getenv("ENV_FILE", ".env"))


class Config:
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]