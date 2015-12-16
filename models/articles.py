from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relation, backref

import sys
sys.path.append("./models/")
import model as Model
from model import model

class articles(Model.Base, model):
    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)
    text = Column(Text)
    created = Column(DateTime, default=model._get_date)
    updated = updated_at = Column(DateTime, onupdate=model._get_date)

    def __init__(self, text):
        super(articles, self).__init__()
        self.text = text

    def setup(self):
        self.filter = filter(self)

    def __repr__(self):
        return "<articles('%s','text()',%s','%s')>" % (self.id, self.created, self.updated)
