from fastapi import FastAPI, APIRouter
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from starlette.responses import HTMLResponse

from app.routes import home

app = FastAPI()

router = APIRouter()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(home.router)

templates = Jinja2Templates(directory="templates")

@router.get ("/html", response_class= HTMLResponse)
async def pure_html():
    html_content="""
    <html>
    <head>
        <title>Juan</title>
    </head>
    <body>
        <h1>Mi html</h1>
    </body>
    </html>
    """
    return HTMLResponse(content=html_content,status_code=200)