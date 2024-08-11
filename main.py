from fastapi import FastAPI, Query
from schemas import Book
from typing import List


app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/item/{name}")
def get_name(name: int, state: str = None):
    # print(name)
    if state is None:
        return {"message": f"Hello {name}"}
    else:
        return {"message": f"Hello {name} - {state}"}


@app.get("/user/{name}/item/{item}")
def get_user_item(name: str, item: int):
    return {"message": f"Hello {name} - {item}"}

@app.post("/book")
def create_book(item: Book):
    return item

@app.get("/books")
def get_books_test(e: List[str] = Query( description='search book')):  #, min_length=2, max_length=5
    print(e)
    return {"e": e}
