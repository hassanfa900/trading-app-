from fastapi import WebSocket
import json

clients = []

async def connect(ws: WebSocket):
    await ws.accept()
    clients.append(ws)

def disconnect(ws: WebSocket):
    if ws in clients:
        clients.remove(ws)

async def broadcast(message: dict):
    data = json.dumps(message)
    for ws in clients:
        await ws.send_text(data)

async def handle_message(ws: WebSocket, data: str):
    # لو حابب تستقبل أوامر من العميل (مثلاً إضافة رمز جديد)
    pass

