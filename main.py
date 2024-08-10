from fastapi import FastAPI
from schemas import Book

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Hello World"}

@app.get("/{name}")
def get_name(name: int, state: str = None):
    if state is None:
        return {"message": f"Hello {name}"}
    else:
        return {"message": f"Hello {name} - {state}"}


@app.get("/user/{name}/item/{item}")
def get_user_item(name: str, item: int):
    return {"message": f"Hello {name} - {item}"}

@app.post("/book")
def create_book(book: Book):
    return book
