from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.connections: dict[int, WebSocket] = {}

    async def connect(self, order_id: int, websocket: WebSocket):
        await websocket.accept()
        self.connections[order_id] = websocket

    def disconnect(self, order_id: int):
        self.connections.pop(order_id, None)

    async def send_to_order(self, order_id: int, message: str):
        websocket = self.connections.get(order_id)

        if websocket:
            await websocket.send_text(message)
