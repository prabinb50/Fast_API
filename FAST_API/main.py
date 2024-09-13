from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

@app.get('/')
def index():
    return {'data':{'name': 'Prabin'}}

@app.get('/about')
def about():
    return {"data":{"about page"}}



# For Query Parameters
@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the database"}
    else:
        return {"data": f"{limit} blogs from the database"}



# For Path Parameters
@app.get("/blog/{id}")
def show(id: int):
    # fetch blog with id = id 
    return{"data": id}

@app.get("/blog/{id}/comments")
def comments():
    # fetch comments of blog with id = id
    return {"data": {"1", "2"}}



# For Request Body
class Blog (BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created with title as {request.title}"}
