from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    username: str = Field(min_length=5, max_length=20)
    email: EmailStr

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    role: int = Field(lt=4, gt=0)

    class Config:
        def __init__(self):
            pass

        from_attributes = True

class UserProfileEdit(BaseModel):
    username: str = Field(min_length=5, max_length=20)
    email: EmailStr

class UserPasswordChange(BaseModel):
    password: str = Field(min_length=8)

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    user_id: int

    class Config:
        def __init__(self):
            pass

        orm_mode = True
