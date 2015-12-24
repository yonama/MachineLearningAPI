import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relation, backref

import sys
sys.path.append("./models/")
import model as Model
from model import model

class article(Model.Base, model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    updated = Column(DateTime, onupdate=datetime.datetime.utcnow)

    def __init__(self, text):
        super(articles, self).__init__()
        self.text = text

    def setup(self):
        self.filter = filter(self)

    def __repr__(self):
        return "<article('%s','text()',%s','%s')>" % (self.id, self.created, self.updated)
