from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
import os

# Load the environment variables
load_dotenv()

# Get the conneciton string from an environment variable.
connection_string = os.getenv('DATABASE_URL', 'sqlite+pysqlite:///database.db')

# Create a connection to the database.
engine = create_engine(connection_string, echo=True)

# Create a session factory.
SessionFactory = sessionmaker(bind=engine)
session = scoped_session(SessionFactory)
