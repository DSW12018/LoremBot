from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import *

database_name = "sqlite:///db.sqlite3"

engine = create_engine(database_name, echo=True)
Session = sessionmaker(bind=engine)
session = Session()
