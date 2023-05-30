import uvicorn
from fastapi import FastAPI

from utils import get_all_names, ModelSchema, Model, most_similarity, add_count

all_terms = []
app = FastAPI()


@app.post("/")
async def add_new_term(info: ModelSchema):
    if info.name in get_all_names(all_terms):
        return {"status code": 404, "info": "this term already exist"}

    obj = Model(**dict(info), cnt=1)
    all_terms.append(obj)

    return {"status code": 201}


@app.get("/")
async def get_all_terms():
    return {"status code": 200, "terms": all_terms}


@app.get("/similarity")
async def find_most_similarity_term(word: str):
    ls = most_similarity(all_terms, word)
    return ls


@app.get("/add_count/")
async def add_count_to_term(name: str):
    return add_count(name, all_terms)


if __name__ == '__main__':
    uvicorn.run("main:app")
