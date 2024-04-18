from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request
from app.routers import model

app = FastAPI()

app.include_router(model.router, tags=["model"], prefix="/model")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def read_root(request: Request):
    # return index.html
    return templates.TemplateResponse("index.html", {"request": request})
