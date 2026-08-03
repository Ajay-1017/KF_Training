# FastAPI Learning Roadmap

## 1. FastAPI Fundamentals

### Topics

- FastAPI project structure
- Routing
- Request & Response Models
- Path & Query Parameters
- Pydantic Validation
- Swagger Documentation (`/docs`)
- Uvicorn

### Tasks

- [X] Create a FastAPI project.
- [X] Build a `/health` endpoint.
- [ ] Build CRUD APIs for users.
- [X] Test APIs using Swagger.
- [ ] Test APIs using Postman.

---

## 2. FastAPI + PostgreSQL

### Topics

- PostgreSQL
- SQLAlchemy ORM
- Alembic Migrations
- CRUD with Database
- Database Relationships
- Environment Variables

### Tasks

#### Products API

- [ ] Add Product
- [ ] Get All Products
- [ ] Get Product by ID
- [ ] Update Product
- [ ] Delete Product

#### Customers API

- [ ] Create Customer
- [ ] Get All Customers
- [ ] Get Customer by ID
- [ ] Update Customer
- [ ] Delete Customer

#### Cart API

- [ ] Create Cart
- [ ] Add Item to Cart
- [ ] Remove Item from Cart
- [ ] View Cart

#### Orders API

- [ ] Place Order
- [ ] View Order
- [ ] View Order History

---

## 3. Business Logic APIs

### Topics

- Service Layer
- Error Handling
- Validation
- JWT Authentication
- Logging

### Tasks

- [ ] Don't allow ordering out-of-stock products.
- [ ] Calculate cart total.
- [ ] Validate product availability.
- [ ] Update stock after purchase.
- [ ] Return meaningful error responses.
- [ ] Protect APIs using JWT authentication.
- [ ] Log API requests and important events.

---
