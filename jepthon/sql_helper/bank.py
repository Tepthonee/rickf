from sqlalchemy import Column, String, UnicodeText

from . import BASE, SESSION


class Bot_Starters(BASE):
    __tablename__ = "bank"
    user_id = Column(String(14), primary_key=True)
    first_name = Column(UnicodeText)
    balance = Column(String(14), primary_key=True)
    bank = Column(UnicodeText)

    def __init__(self, user_id, first_name, balance, bank):
        self.user_id = str(user_id)
        self.first_name = first_name
        self.balance = int(balance)
        self.bank = bank


bank.__table__.create(checkfirst=True)


def add_bank(
    user_id,
    first_name,
    balance,
    bank,
):
    to_check = get_starter_details(user_id)
    if not to_check:
        user = bank(str(user_id), first_name, int(balance), bank)
        SESSION.add(user)
        SESSION.commit()
        return True
    rem = SESSION.query(bank).get(str(user_id))
    SESSION.delete(rem)
    SESSION.commit()
    user = bank(str(user_id), first_name, int(balance), bank)
    SESSION.add(user)
    SESSION.commit()
    return True


def del_bank(user_id):
    to_check = get_starter_details(user_id)
    if not to_check:
        return False
    rem = SESSION.query(bank).get(str(user_id))
    SESSION.delete(rem)
    SESSION.commit()
    return True


def get_bank(user_id):
    try:
        if _result := SESSION.query(bank).get(str(user_id)):
            return _result
        return None
    finally:
        SESSION.close()


def get_all_bank():
    try:
        return SESSION.query(bank).all()
    except BaseException:
        return None
    finally:
        SESSION.close()
