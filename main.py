from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def read_root():
    return FileResponse("index.html")

@app.get("/map")
async def read_splash():
    return FileResponse("map.html")

# serve the favicon from /static/artificial-intelligence.png
@app.get("/favicon.ico")
async def read_favicon():
    return FileResponse("static/artificial-intelligence.png")