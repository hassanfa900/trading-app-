from fastapi import FastAPI, WebSocket
from app import websocket_manager, api_routes

app = FastAPI()

# REST API routes
app.include_router(api_routes.router)

# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await websocket_manager.connect(ws)
    try:
        while True:
            data = await ws.receive_text()
            await websocket_manager.handle_message(ws, data)
    except Exception:
        websocket_manager.disconnect(ws)

