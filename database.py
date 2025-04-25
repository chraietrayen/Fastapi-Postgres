from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Connection URL - adjust credentials as needed
URL_DATABASE = 'postgresql://postgres:postgres@localhost:5432/quizApp'

# Create engine with additional parameters for better error handling
engine = create_engine(
    URL_DATABASE,
    pool_pre_ping=True,  # Checks connection before using
    echo=True  # Shows SQL queries in console (helpful for debugging)
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()