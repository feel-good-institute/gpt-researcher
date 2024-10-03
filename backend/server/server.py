from fastapi import FastAPI, WebSocket
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from backend.config import STATIC_PATH
from backend.routes import router

app = FastAPI()

app.mount("/static", StaticFiles(directory=STATIC_PATH), name="static")
app.include_router(router)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")

@app.get("/")
async def read_index():
    return FileResponse(STATIC_PATH + '/index.html')
