from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# url = postgresql://{username}:{password}@{hostname}:{port}/{db_name}
db_url = "postgresql://aayushsingh:postgres@localhost:5432/postgres"
engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)