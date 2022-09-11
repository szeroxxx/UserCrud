from pydantic import BaseModel
class User(BaseModel):
    name:str
    email:str
    phone:int
    city:str
    state:str
    country:str
    address:str
    zipcode:int
    password:str

class UpdateUser(BaseModel):
    name:str
    email:str
    phone:int
    city:str
    state:str
    country:str
    address:str
    zipcode:int
    password:str

    