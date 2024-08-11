from fastapi import FastAPI, Query, Path
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

# работа с path параметрами
@app.get("/user/{name}/item/{item}")
def get_user_item(name: str, item: int):
    return {"message": f"Hello {name} - {item}"}

# работа с body и post параметрами
@app.post("/book")
def create_book(item: Book):
    return item

# работа с query параметрами
@app.get("/books")
def get_books_test(e: List[str] = Query( description='search book')):  #, min_length=2, max_length=5
    print(e)
    return {"e": e}

# работа с query параметрами и Path параметрами
@app.get("/book/{book_id}")
def get_book(book_id: int = Path(..., gt=1, le=5), pages: int = Query(None, gt=10, lt=100)):
    return {"book_id": book_id, "pages": pages}
