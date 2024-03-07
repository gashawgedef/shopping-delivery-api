from typing import Optional
from pydantic import BaseModel, Field


class SignupModel(BaseModel):
    username: str
    email: str
    password: str
    is_active: Optional[bool]
    is_staff: Optional[bool]

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                "username": "gashaegedef",
                "email": "gashawgedef@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = 'c299dea258b08b4a4bfa2380f7b56df5a82f4c41850e28fe059350d1541e18e8'


class LoginModel(BaseModel):
    username: str
    password: str
