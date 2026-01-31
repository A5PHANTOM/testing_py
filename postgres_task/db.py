from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

DB_URL = "postgresql://mac@localhost:5432/college_db"

engine = create_engine(DB_URL,echo=True)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
