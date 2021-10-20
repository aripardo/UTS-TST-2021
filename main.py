#Ari Pardomuan Manurung
#18219045

import json
import jwt
from fastapi import FastAPI, HTTPException, Header
from fastapi.params import Depends
from pydantic import BaseModel
from typing import Optional
with open("menu.json", "r") as read_file:
    data = json.load(read_file)

app = FastAPI()

class Menu(BaseModel):
    id: Optional[str] = None
    name: str
    
class User(BaseModel):
    username: str
    password: str

@app.get("/allmenu")
async def getall_menu(authorization: Optional[str] = Header(None)):
    token = authorization[7:]
    try:
        payload = jwt.decode(token, "SECRET", algorithms="HS256")
        if payload['username'] != "asdf":
            raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    except:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    return data['menu']

@app.get('/menu/{item_id}')
async def read_menu(item_id: int, authorization: Optional[str] = Header(None)):
    if authorization == None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    token = authorization[7:]
    try:
        payload = jwt.decode(token, "SECRET", algorithms="HS256")
        if payload['username'] != "asdf":
            raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    except:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            return menu_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
    )

@app.post("/menu")
async def add_menu(item: Menu, authorization: Optional[str] = Header(None)):
    if authorization == None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    token = authorization[7:]
    try:
        payload = jwt.decode(token, "SECRET", algorithms="HS256")
        if payload['username'] != "asdf":
            raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    except:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    newId = data['menu'][len(data['menu']) - 1]['id'] + 1
    item.id = newId
    data['menu'].append(item.dict())
    return item

@app.put("/menu/{item_id}")
async def add_menu(item_id: int, item: Menu, authorization: Optional[str] = Header(None)):
    if authorization == None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    token = authorization[7:]
    try:
        payload = jwt.decode(token, "SECRET", algorithms="HS256")
        if payload['username'] != "asdf":
            raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    except:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            menu_item['name'] = item.name
            return menu_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
    )
@app.delete("/menu/{item_id}")
async def delete_menu(item_id: int, authorization: Optional[str] = Header(None)):
    if authorization == None:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    token = authorization[7:]
    try:
        payload = jwt.decode(token, "SECRET", algorithms="HS256")
        if payload['username'] != "asdf":
            raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    except:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized User"
        )
    newMenus = []
    deletedMenu = None
    found = False
    for menu_item in data['menu']:
        if int(menu_item['id']) != item_id:
            newMenus.append(menu_item)
        else:
            deletedMenu = menu_item
            found = True
    data['menu'] = newMenus
    if not found:
        raise HTTPException(
            status_code=404, detail=f'Item not found'
        )
    return deletedMenu

@app.post("/login")
async def login_for_access_token(user: User):
    if user.username =="asdf" and user.password=="asdf":
        payload = {
            "username": user.username,
        }
        token = jwt.encode(payload, "SECRET", algorithm="HS256")
        return {
            "token": token
        }
    raise HTTPException(
        status_code=400, detail="Wrong credential"
    )
        


