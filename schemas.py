from pydantic import BaseModel, validator
from datetime import date
from typing import List

class Genres(BaseModel):
    name: str

class Author(BaseModel):
    first_name: str
    last_name: str
    age: int

#validator - но говорят по документации его лучше уже не использовать 
    @validator('age')
    def check_age(cls, v):
        if v < 15:
            raise ValueError('Age must be positive')
        return v

class Book(BaseModel):
    title: str
    writer: str
    duration: str
    date: date
    summary: str
    genres: List[Genres]
    pages: int