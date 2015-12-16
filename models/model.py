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

Base = declarative_base()
config = configparser.ConfigParser()
config.read('models/bootstrap.ini')

class model(actor):
    session = sessionmaker(bind=create_engine("mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8&use_unicode=1" % (config['DataBase']['user'],config['DataBase']['password'],config['DataBase']['host'],config['DataBase']['port'],config['DataBase']['database']) , echo=True))

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
        cls.sesion.commit()

    @classmethod
    def rollback(cls):
        cls.sesion.rollback()

    @classmethod
    def add_all(cls, array):
        cls.session.add_all(array)

    @staticmethod
    def _get_date():
        return datetime.datetime.now()

    def query(self, *args):
        self.session.query(*args)

    def save(self):
        self.session.add(self)
        self.commit()
