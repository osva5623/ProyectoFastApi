#python
from typing import Optional
#pydantic
from pydantic import BaseModel
#Fastapi
from fastapi import FastAPI
from fastapi import Body,Query,Path

app=FastAPI()

#models

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
