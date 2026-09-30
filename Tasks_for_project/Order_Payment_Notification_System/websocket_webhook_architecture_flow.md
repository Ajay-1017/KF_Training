# Order → Payment → Webhook → Database → WebSocket → Browser

```text
┌─────────────────────────────────────────────────────────────┐
│                         STEP 1                              │
│                     USER CREATES ORDER                      │
└────────────────────────────┬────────────────────────────────┘
                             │
                             │ POST /orders
                             ▼
                      ┌───────────────┐
                      │    FastAPI    │
                      │    main.py    │
                      └───────┬───────┘
                              │
                              │ SQLAlchemy Session
                              ▼
                      ┌───────────────┐
                      │  PostgreSQL   │
                      │               │
                      │ Order #8      │
                      │ PENDING       │
                      └───────────────┘


┌─────────────────────────────────────────────────────────────┐
│                         STEP 2                              │
│                  BROWSER OPENS WEBSOCKET                    │
└────────────────────────────┬────────────────────────────────┘
                             │
                             │ /ws/8
                             ▼
                      ┌───────────────┐
                      │    FastAPI    │
                      └───────┬───────┘
                              │
                              │ connect()
                              ▼
                   ┌────────────────────┐
                   │ ConnectionManager  │
                   │                    │
                   │ 8 → WebSocket      │
                   └────────────────────┘


┌─────────────────────────────────────────────────────────────┐
│                         STEP 3                              │
│                  PAYMENT IS COMPLETED                       │
└────────────────────────────┬────────────────────────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │ Payment Provider       │
                 │ payment_simulator.py   │
                 └────────────┬───────────┘
                              │
                              │ POST /webhooks/payment
                              │ { order_id: 8 }
                              ▼
                       ┌───────────────┐
                       │    FastAPI    │
                       └───────┬───────┘
                               │
                               │ find order 8
                               ▼
                       ┌───────────────┐
                       │  PostgreSQL   │
                       │               │
                       │ PENDING       │
                       │     ↓         │
                       │    PAID       │s
                       └───────┬───────┘
                               │
                               │ notify
                               ▼
                    ┌────────────────────┐
                    │ ConnectionManager  │
                    │                    │
                    │ find connection 8  │
                    └──────────┬─────────┘
                               │
                               │ send_text()
                               ▼
                        ┌─────────────┐
                        │  WebSocket  │
                        └──────┬──────┘
                               │
                               │ message
                               ▼
                        ┌─────────────┐
                        │   Browser   │
                        │  test.html  │
                        └─────────────┘
```
