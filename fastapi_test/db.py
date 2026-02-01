from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base

url = "postgresql://mac@localhost:5432/school_db"

engine = create_engine(url,echo=True)
sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


