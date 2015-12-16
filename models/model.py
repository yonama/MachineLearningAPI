#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
import glob
import os.path
import codecs
import re
import configparser

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from actor import actor
from filters.model_filter import model_filter as filter

config = configparser.ConfigParser()
config.read('models/bootstrap.ini')

Base = declarative_base()
Engine = create_engine("mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8&use_unicode=1" % (config['DataBase']['user'],config['DataBase']['password'],config['DataBase']['host'],config['DataBase']['port'],config['DataBase']['database']) , echo=True)

class model(actor):
    session = sessionmaker(bind=Engine)()

    def setup(self):
        self.filter = filter(self)

    @abstractmethod
    def save_befour_action(self):
        raise NotImplementedError()
    @abstractmethod
    def save_after_action(self):
        raise NotImplementedError()
    @abstractmethod
    def save_around_action(self):
        raise NotImplementedError()
    @abstractmethod
    def find_befour_action(self):
        raise NotImplementedError()
    @abstractmethod
    def find_after_action(self):
        raise NotImplementedError()
    @abstractmethod
    def find_around_action(self):
        raise NotImplementedError()

    @classmethod
    def commit(cls):
        cls.session.commit()

    @classmethod
    def rollback(cls):
        cls.session.rollback()

    @classmethod
    def add_all(cls, array):
        cls.session.add_all(array)

    @staticmethod
    def get_date():
        return datetime.datetime.now()

    '''
    @classmethod
    def query(cls, *args):
        cls.session.query(*args)
    '''

    def save(self):
        self.session.add(self)
        self.commit()
