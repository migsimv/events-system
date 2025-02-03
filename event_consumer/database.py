from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

class Database:
    def __init__(self, database_url: str):
        self.engine = create_engine(database_url)
        Base.metadata.create_all(self.engine)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def get_session(self):
        session = self.SessionLocal()
        try:
            yield session
        finally:
            session.close()
