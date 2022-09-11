from distutils.version import StrictVersion
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer, String
from db import meta

users = Table(
    'users',meta,
    Column('id',Integer, primary_key=True ),
    Column('name',String(255)),
    Column('email',String(255)),
    Column('country',String(255)),
    Column('password',String(255)),
    Column('phone',Integer),
    Column('zipcode',Integer),
    Column('state',String(255)),
    Column('address',String(255)),
    Column('city',String(255)),
)