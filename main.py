#python
from typing import Optional
from enum import Enum
#pydantic
from pydantic import BaseModel
from pydantic import Field
#Fastapi
from fastapi import FastAPI
from fastapi import Body,Query,Path

app=FastAPI()

#models

class HairColor(Enum):
    white="white"
    brown="brown"
    black="black"
    blonde="blonde"
    red="red"

class Location(BaseModel):
    city:str
    state:str
    country:str

class Person(BaseModel):
    first_name:str=Field(
        ...,
        min_length=1,
        max_length=50,
        example="miguel")
    last_name:str=Field(
        ...,
        min_length=1,
        max_length=50,
        example="torres")
    age:int=Field(
        ...,
        gt=0,
        le=115
    )
    head_color:Optional[HairColor]=Field(
        default=None,
        example=HairColor.black)
    is_married:Optional[bool]=Field(
        default=None,
        expample=False
    )
    # class Config: 
    #     schema_extra = {
    #         "example": {
    #             "first_name": "Facundo",
    #             "last_name": "García Martoni",
    #             "age": 21, 
    #             "hair_color": "blonde",
    #             "is_married": False
    #         }
    #     }    

@app.get("/")
def home():
    return {"hello":"world"}

@app.post("/person/new")
def create_person(person:Person=Body(...)):
    return person

# Validaciones: Query Parameters
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

# Validaciones: Path Parameters
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

# Validaciones: Request Body
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