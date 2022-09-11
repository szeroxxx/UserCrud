from sqlalchemy import create_engine,MetaData
meta = MetaData()

engine = create_engine("mysql+mysqlconnector://root@localhost:3307/crudoperation?charset=utf8")
conn = engine.connect()

