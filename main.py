from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()



#creamos una clase user
class User (BaseModel):
    id:int
    name:str
    surname:str
    url:str
    age:int
    language:str
    
#creamos la lista
user_list=[User(id=1,name='eva',surname='Hachero',url='hachero@avaya.com',age=53,language='spanish'),
           User(id=2,name='Juan Antonio',surname='Estival',url='estival@google.com',age=51, language='english'),
           User(id=3,name='Miguel', surname='Pascual', url='pascual@avaya.com',age=55,language='spanish')]


#traer la lista completa
@app.get("/users")

async def users():
    return (user_list)

#traer un usuario por query
@app.get("/users/")

async def user(id:int):
    for index,register in enumerate(user_list):
        if id==register.id:
            return(register)   
#para invocarlo: http://server/users/1    

 #traer un usuario por path
@app.get("/users/{id}")

async def user(id:int):
    for index,register in enumerate(user_list):
        if id==register.id:
            return(register)   
#para invocarlo: http://server/users/?id=1   

#añadir un usuario
@app.post("/user/")

async def add_user(new_user:User):
    user_list.append(new_user)

#actualizar un usuario
@app.put("/user/")

async def update(user_update:User):
    for index, register in enumerate(user_list):
        if register.id==user_update.id:
            user_list[index]=user_update


    
