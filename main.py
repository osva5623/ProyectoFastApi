#python
from typing import Optional
#pydantic
from pydantic import BaseModel
#Fastapi
from fastapi import FastAPI
from fastapi import Body

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

@app.get("/person/new")
def create_person(person:Person=Body(...)):
    return person