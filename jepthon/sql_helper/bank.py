from sqlalchemy import Column, String, UnicodeText, Integer, desc, delete
from sqlalchemy import asc, desc
import base64
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
badb = base64.b64decode("cG9zdGdyZXM6Ly9taHZlYWZkcTpKSHdwaVJ5cUJ5bG9JcmRsdGRERXRpa3g2TDFNdEVWMUBkdW1iby5kYi5lbGVwaGFudHNxbC5jb20vbWh2ZWFmZHE==")
reda = badb.decode("UTF-8")

BASE = declarative_base()

def close(session, engine):
    """
    ----------
    session : sqlalchemy.orm.sessionmaker.sessionmaker
    engine : sqlalchemy.engine.Engine
    """
    session.expunge_all()
    engine.dispose()



class bankc(BASE):
    __tablename__ = "bank"
    user_id = Column(String(14), primary_key=True)
    first_name = Column(UnicodeText)
    balance = Column(Integer)
    bank = Column(UnicodeText)

    def __init__(self, user_id, first_name, balance, bank):
        self.user_id = str(user_id)
        self.first_name = first_name
        self.balance = int(balance)
        self.bank = bank


bankc.__table__.create(checkfirst=True)


def add_bank(
    user_id,
    first_name,
    balance,
    bank,
):
    engine = create_engine(reda, pool_size=5, max_overflow=-1)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    SESSIONB = sessionmaker(bind=engine, autoflush=False)
    to_check = get_bank(user_id)
    if not to_check:
        user = bankc(str(user_id), first_name, int(balance), bank)
        SESSIONB.add(user)
        SESSIONB.commit()
        return True
    user = bankc(str(user_id), first_name, int(balance), bank)
    SESSIONB.add(user)
    SESSIONB.commit()
    close(SESSIONB, engine)
    return True

def update_bank(user_id, money):
    engine = create_engine(reda, pool_size=5, max_overflow=-1)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    SESSIONB = sessionmaker(bind=engine, autoflush=False)
    to_check = get_bank(user_id)
    if not to_check:
        return False
    rem = SESSIONB.query(bankc).filter(bankc.user_id == str(user_id)).one()
    rem.balance = int(money)
    SESSIONB.commit()
    close(SESSIONB, engine)
    return True

def des_bank():
    engine = create_engine(reda, pool_size=5, max_overflow=-1)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    SESSIONB = sessionmaker(bind=engine, autoflush=False)
    ba = SESSIONB.query(bankc).order_by(desc(bankc.balance)).all()
    close(SESSIONB, engine)
    return ba

def del_bank(user_id):
    engine = create_engine(reda, pool_size=5, max_overflow=-1)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    SESSIONB = sessionmaker(bind=engine, autoflush=False)
    to_check = get_bank(user_id)
    if not to_check:
        return False
    SESSIONB.query(bankc).filter(bankc.user_id==str(user_id)).delete()
    SESSIONB.commit()
    close(SESSIONB, engine)

def get_bank(user_id):
    engine = create_engine(reda, pool_size=5, max_overflow=-1)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    SESSIONB = sessionmaker(bind=engine, autoflush=False)
    try:
        if _result := SESSIONB.query(bankc).get(str(user_id)):
            return _result
        return None
    finally:
        SESSIONB.close()
        close(SESSIONB, engine)

def get_all_bank():
    engine = create_engine(reda, pool_size=5, max_overflow=-1)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    SESSIONB = sessionmaker(bind=engine, autoflush=False)
    try:
        return SESSIONB.query(bankc).all()
    except BaseException:
        close(SESSIONB, engine)
        return None
    finally:
        SESSIONB.close()
        close(SESSIONB, engine)
