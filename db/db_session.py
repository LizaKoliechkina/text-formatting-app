from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import config

engine = create_engine(config.SQLALCHEMY_DB_URI)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def get_db_session():
    db = Session()
    try:
        yield db
    finally:
        db.close()
