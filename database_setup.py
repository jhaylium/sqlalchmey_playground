import sys, json
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'

class MenuItem(Base):
    __tablename = 'menu_item'




configs = json.load(open('config.json'))
username = configs['username']
password = configs['password']
server_name = configs['server_name']
port = configs['port']
dbname = configs['dbname']
conn_str = '{un}:{pw}@{host}:{port}/{db}'.format(un=username, pw=password, host=server_name, port=port, db=dbname)
print(conn_str)
# engine = create_engine('postgresql+psycopg2://' + conn_str)