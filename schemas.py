from typing import Optional
from pydantic import BaseModel


class SignupModel(BaseModel):
    username:str
    email:str
    password:str
    is_active:Optional[bool]
    is_staff:Optional[bool]
    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "username":"gashaegedef",
                "email":"gashawgedef@gmail.com",
                "password":"password",
                "is_staff":False,
                "is_Active":True
            }
        }