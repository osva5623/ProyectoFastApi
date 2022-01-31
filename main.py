#python
from typing import Optional
#pydantic
from pydantic import BaseModel
#Fastapi
from fastapi import FastAPI
from fastapi import Body,Query,Path

app=FastAPI()

#models
class Location(BaseModel):
    city:str
    state:str
    country:str

class Person(BaseModel):
    first_name:str
    last_name:str
    age:int
    head_color:Optional[int]=None
    is_married:Optional[bool]=None

@app.get("/")
def home():
    return {"hello":"world"}

@app.post("/person/new")
def create_person(person:Person=Body(...)):
    return person

@app.get("/person/detail")
def show_person(
    name:Optional[str]=Query(
        None, 
        min_length=1,
        max_length=50,
        title="Person name",
        description="This is a person name.It's between 1 and 50 characters"
        ),
    age :str =Query(
        ...,
        title="Person age",
        description="This is a person age.It's required"
        )
):
    return{name:age}

@app.get("/person/detail/{person_id}")
def show_person(
    person_id:int=Path(
        ...,
        gt=0,
        title="Person id",
        description="This is a person id,It's greater than 0"
        )
):
    return{person_id:"It exists!"}

@app.put("/person/{person_id}")
def update_person(
    person_id:int=Path(
        ...,
        title="Person id",
        description="This is a person id",
        gt=0
        ),
        person:Person=Body(...),
        location:Location=Body(...)

):
    results=person.dict()
    results.update(location.dict())
    return results