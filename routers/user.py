
from typing import Union
from fastapi import APIRouter,Request
from db import conn
from models.index import users
from schemas.index import User, UpdateUser
from sqlalchemy.orm import Session
user = APIRouter()

@user.get("/")
def listing(limit: Union[int, None] = None,off_set: Union[int, None] = None,name: Union[str, None] = None,email: Union[str, None] = None,phone: Union[int, None] = None,
city: Union[str, None] = None,state: Union[str, None] = None,country: Union[str, None] = None,zipcode: Union[int, None] = None
,address: Union[str, None] = None,sorting: Union[bool, None] = False):
    if name:
        if sorting == True:
            data = conn.execute(users.select().where(users.c.name==name).order_by(users.c.name.desc())).fetchall()
        else:
            data = conn.execute(users.select().where(users.c.name==name)).fetchall()

    if email:
        if sorting == True:
            data = conn.execute(users.select().where(users.c.email==email).order_by(users.c.email.desc())).fetchall()
        else:
            data = conn.execute(users.select().where(users.c.email==email)).fetchall()
    if phone:
        if sorting == True:
            data = conn.execute(users.select().where(users.c.phone==phone).order_by(users.c.phone.desc())).fetchall()
        else:
            data = conn.execute(users.select().where(users.c.phone==phone)).fetchall()
    if city:
        if sorting == True:
            data = conn.execute(users.select().where(users.c.city==city).order_by(users.c.city.desc())).fetchall()
        else:
            data = conn.execute(users.select().where(users.c.city==city)).fetchall()
    if state:
        if sorting == True:
            data = conn.execute(users.select().where(users.c.state==state).order_by(users.c.state.desc())).fetchall()
        else:
            data = conn.execute(users.select().where(users.c.state==state)).fetchall()
    if country:
        if sorting == True:
            data = conn.execute(users.select().where(users.c.country==country).order_by(users.c.country.desc())).fetchall()
        else:
            data = conn.execute(users.select().where(users.c.country==country)).fetchall()
    if zipcode:
        if sorting == True:
            data = conn.execute(users.select().where(users.c.zipcode==zipcode).order_by(users.c.zipcode.desc())).fetchall()
        else:
            data = conn.execute(users.select().where(users.c.zipcode==zipcode)).fetchall()
    if address:
        if sorting == True:
            data = conn.execute(users.select().where(users.c.address==address).order_by(users.c.address.desc())).fetchall()
        else:
            data = conn.execute(users.select().where(users.c.address==address)).fetchall()
    else:
        if sorting == True:
            data = conn.execute(users.select().order_by(users.c.id.desc())).fetchall()
        else:
            data = conn.execute(users.select().limit(limit).offset(off_set)).fetchall()
    return data

@user.get("/{id}")
def find_user(id:int):
    data = conn.execute(users.select().where(users.c.id==id)).fetchall()
    return data

@user.post("/create_user/")
def create_user(name: Union[str, None] = None,email: Union[str, None] = None,phone: Union[int, None] = None,
city: Union[str, None] = None,state: Union[str, None] = None,country: Union[str, None] = None,zipcode: Union[int, None] = None
,address: Union[str, None] = None,password: Union[str, None] = None):
    conn.execute(users.insert().values(
            name=name,
            email=email,
            phone=phone,
            city=city,
            state=state,
            country=country,
            address=address,
            zipcode=zipcode,
            password=password,
        ))
    data = conn.execute(users.select().where(users.c.name==name)).fetchall()
    return data

@user.put("/{id}")
async def update_user(request: Request):
    data = await request.json()
    conn.execute(users.update().values(
        name=data["name"],
        email=data["email"],
        phone=data["phone"],
        city=data["city"],
        state=data["state"],
        country=data["country"],
        address=data["address"],
        zipcode=data["zipcode"],
        password=data["password"],
    ).where(users.c.id==5))
    data = conn.execute(users.select()).fetchall()
    return data

@user.delete("/{id}")
def delete_user(id:int):
    conn.execute(users.delete().where(users.c.id==id))
    data = conn.execute(users.select()).fetchall()
    return data
