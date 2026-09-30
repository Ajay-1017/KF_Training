from pydantic import BaseModel


class CreateOrder(BaseModel):
    product_name: str
    amount: float


class PaymentWebhook(BaseModel):
    order_id: int
    status: str
