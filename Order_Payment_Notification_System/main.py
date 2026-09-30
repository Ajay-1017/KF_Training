from typing import Annotated

from fastapi import Depends, FastAPI, WebSocket, WebSocketDisconnect
from sqlalchemy import select
from sqlalchemy.orm import Session

import models
from connection_manager import ConnectionManager
from database import Base, engine, get_session
from schemas import CreateOrder, PaymentWebhook

Base.metadata.create_all(bind=engine)

app = FastAPI()

manager = ConnectionManager()


@app.post("/orders")
def create_order(
    order: CreateOrder,
    db: Annotated[Session, Depends(get_session)],
):
    new_order = models.Order(
        product_name=order.product_name,
        amount=order.amount,
        status="PENDING",
    )

    db.add(new_order)
    db.commit()
    db.refresh(new_order)

    return new_order


@app.post("/webhooks/payment")
async def payment_webhook(
    payment: PaymentWebhook,
    db: Annotated[Session, Depends(get_session)],
):
    result = db.execute(
        select(models.Order).where(
            models.Order.id == payment.order_id
        )
    )

    order = result.scalars().first()

    if not order:
        return {"message": "Order not found"}

    order.status = "PAID"

    db.commit()
    db.refresh(order)

    await manager.send_to_order(
        payment.order_id,
        f"Payment paid for order {payment.order_id}",
    )

    return {
        "message": "Payment processed",
        "order_id": order.id,
        "status": order.status,
    }


@app.websocket("/ws/{order_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    order_id: int,
):
    await manager.connect(order_id, websocket)

    await websocket.send_text(
        f"Connected to order {order_id}"
    )

    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        manager.disconnect(order_id)
