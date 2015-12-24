import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relation, backref

import sys
sys.path.append("./models/")
import model as Model
from model import model
import transaction

class visit_history(Model.Base, model):
    __tablename__ = 'visit_histories'

    id = Column(Integer, primary_key=True)
    article_id = Column(Integer)
    transaction_id = Column(Integer, ForeignKey('transactions.id'))
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.datetime.utcnow)

    transactions = relation("transaction", backref=backref('visit_histories', order_by=id))

    def __init__(self, article_id, transaction_id):
        super(visit_history, self).__init__()
        self.article_id = article_id
        self.transaction_id = transaction_id

    def setup(self):
        self.filter = filter(self)

    def __repr__(self):
        return "<visit_histories('%d','%d','%s','%s')>" % (self.id, self.transaction_id, self.created, self.updated)
