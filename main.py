from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/css",StaticFiles(directory="css"),name="css")

@app.get("/")
def main(request: Request):
 return templates.TemplateResponse("index.html", {"request": request})


@app.get("/login")
def login(request: Request):
 return templates.TemplateResponse("login.html", {"request": request})
 
@app.get("/register")
def register(request: Request):
 return templates.TemplateResponse("register.html", {"request": request})

