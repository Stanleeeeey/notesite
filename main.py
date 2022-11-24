from fastapi import FastAPI, Response, Form, Request

from typing import Union
from fastapi.responses import HTMLResponse
import os
from pydantic import BaseModel
from sql import createpost, get_content
from fastapi.templating import Jinja2Templates
import jinja2
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get('/',  response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("main.html", {"request": request} )

@app.post('/add',   response_class=HTMLResponse)
async def add(request: Request, content: str = Form(...)):
    url = createpost(content)
    
    context = {'request': request, "ans": content, 'url' : url}

    return templates.TemplateResponse("ans.html", context )

@app.get('/{id}',   response_class=HTMLResponse)
async def getmessgae(id, request: Request,):
    context = {'request': request, 'x': get_content(id)}
    return templates.TemplateResponse("post.html", context)

@app.get('/edit/{id}',   response_class=HTMLResponse)
async def getmessgae(id, request: Request,):
    context = {'request': request, 'x': get_content(id)}
    return templates.TemplateResponse("edit.html", context)