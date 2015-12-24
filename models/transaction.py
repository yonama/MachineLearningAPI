import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy import event
from sqlalchemy.orm import relation, backref

import sys
sys.path.append("./models/")
import model as Model
from model import model
import visit_history

class transaction(Model.Base, model):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    ipadress = Column(Text)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.datetime.utcnow)

    #visit_histories = relation("visit_history", order_by="visit_history.id", backref="transactions", cascade="all, delete, delete-orphan")

    def validate_ipaddress(target, value, oldvalue, initiator):
        #validation処理
        return value

    def __init__(self, user_id, ipadress):
        super(transaction, self).__init__()
        self.user_id = user_id
        self.ipadress = ipadress
        #event.listen(self.ipadress, 'set', self.validate_ipaddress, retval=True)

    def setup(self):
        self.filter = filter(self)

    def __repr__(self):
        return "<transaction('%d','%d','%s','%s','%s')>" % (self.id, self.user_id, self.ipadress, self.created, self.updated)
