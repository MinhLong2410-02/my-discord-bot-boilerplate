# db/sqlalchemy/database.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.getenv("POSTGRES_URL", "postgresql://user:password@localhost/dbname")

# Create the engine
engine = create_engine(DATABASE_URL, echo=False)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency or helper that yields a database session.
    Example usage:
        with get_db() as db:
            # db is a session
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
