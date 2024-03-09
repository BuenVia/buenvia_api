from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = "sqlite:///./buenvia.db"

engine = create_engine(db_url)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
