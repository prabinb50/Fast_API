from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/blog")
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {"data": f"{limit} published blogs from the database"}
    else:
        return {"data": f"{limit} blogs from the database"}