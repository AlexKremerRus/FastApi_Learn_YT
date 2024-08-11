from fastapi import FastAPI, Query, Path, Body
from schemas import Book, Author, AuthorOut
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
# добавляем респонс модель для отображения респонса в доке и валидации ответа согласно модели, response_model_exclude_defaults - не показывает в респонс модели дефолтные значения пустые например
# response_model_exclude='summary' - не показывает в респонс модели summary
@app.post("/book", response_model=Book, response_model_exclude_defaults=True, response_model_exclude={'summary'})
def create_book(item: Book, author: Author, quantity: int = Body(...)):
    # return {"item": item, "author": author, "quantity": quantity}
    return item

# создания Автора c Body параметрами with embed
@app.post("/author", response_model=AuthorOut)
def create_author(author: Author = Body(..., embed=True)):
    autor_dict = author.model_dump()
    autor_dict['id'] = 1
    return autor_dict 

# работа с query параметрами
@app.get("/books")
def get_books_test(e: List[str] = Query( description='search book')):  #, min_length=2, max_length=5
    print(e)
    return {"e": e}

# работа с query параметрами и Path параметрами
@app.get("/book/{book_id}")
def get_book(book_id: int = Path(..., gt=1, le=5), pages: int = Query(None, gt=10, lt=100)):
    return {"book_id": book_id, "pages": pages}
