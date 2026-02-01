from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DB_URL = "postgresql://mac@localhost:5432/students_db"

engine = create_engine(DB_URL,echo=True)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()