from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define the database URI (SQLite in this case)
DATABASE_URL = "sqlite:///./rps_battle.db"  # Change this for other databases

# Create engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Base class for your models
Base = declarative_base()

# Create a session maker
Session = sessionmaker(bind=engine)

# This will create tables in the database if they don't exist
Base.metadata.create_all(bind=engine)