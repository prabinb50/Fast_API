# post method -> used for create something
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Blog (BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(request: Blog):
    return {"data": f"Blog is created with tile as {request.title}"}