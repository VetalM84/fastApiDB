from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./db.db"
SQLALCHEMY_DATABASE_URL = "mysql+mysqldb://python:kX6rK6eW8ycW8v@185.219.41.251:3306/fastapi"
# DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost:5432/fastapi"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
