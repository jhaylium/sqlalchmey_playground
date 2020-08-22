from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem, Employee, Address
import json

configs = json.load(open('config.json'))
username = configs['username']
password = configs['password']
server_name = configs['server_name']
port = configs['port']
dbname = configs['dbname']
conn_str = '{un}:{pw}@{host}:{port}/{db}'.format(un=username, pw=password, host=server_name, port=port, db=dbname)

engine = create_engine('postgresql+psycopg2://' + conn_str)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
first_rest = Restaurant(name="Pizza Palace")
session.add(first_rest)
session.commit()
session.query(Restaurant).all()
cheese_pizza = MenuItem(name='Cheese Pizza', description='Pizza cheese Only', course='Entree', price="$8.99",
                       restaurant=first_rest)
session.commit()
newEmployee = Employee(name='Rebecca Allen')
rebeccaAddress = Address(street="512 Sycamore Road", zip= "02001", employee=newEmployee)
session.commit()
