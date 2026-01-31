# postgresql://username:password@host:port/database

# username → your mac username # password → empty (by default) # host → localhost # port → 5432


# ❌ psycopg2-binary → PostgreSQL driver

#1#

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base,sessionmaker

DATABASE_URL = "postgresql://mac@localhost:5432/student_db"

engine = create_engine(DATABASE_URL,echo= True)

sessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
