from pydantic import BaseModel, validator,field_validator, Field
from datetime import date
from typing import List

class Genres(BaseModel):
    name: str

class Author(BaseModel):
    first_name: str
    last_name: str
    age: int

#field_validator - для валидации данных
    @field_validator('age')
    def check_age(cls, v):
        if v < 15:
            raise ValueError('Нельзя чтобы возраст был меньше 15')
        return v

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genres]
    pages: int = Field(..., gt=10, lt=1000, description="не может быть меньше 10 и больше 1000")