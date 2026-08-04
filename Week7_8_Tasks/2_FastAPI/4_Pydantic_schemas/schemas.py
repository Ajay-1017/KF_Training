from pydantic import BaseModel , ConfigDict , Field

# FLOW :

# HTTP Request (JSON , URL , QUERY PARAMS)
#       │
#       ▼
# FastAPI reads your function signature
#       │
#       ├── int      → convert to int
#       ├── str      → convert to str
#       ├── float    → convert to float
#       ├── bool     → convert to bool
#       └── BaseModel → create a Python object using Pydantic
#       │
#       ▼
# Calls your function with Python values


# Client
#    │
#    │ JSON
#    ▼
# Uvicorn
#    │
#    ▼
# FastAPI
#    │
#    │ sees Product(BaseModel)
#    ▼
# Pydantic
#    │
#    │ JSON → Product object
#    ▼
# Product(
#     product_name="Laptop",
#     category="Electronics",
#     unit_price=50000
# )
#    │
#    ▼
# FastAPI
#    │
#    ▼
# create_product(product)


class PostBase(BaseModel):
    title : str = Field(min_length=1 , max_length=100)
    content : str = Field(min_length= 1)
    author : str = Field(min_length=1 , max_length = 50) 

class PostCreate(PostBase):
    pass

class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes = True) 
                            #       |
                            # It tells pydantic that can read data from objects with attributes not just dictionaries  

# 1. Without from_attributes=True :

#     SQLAlchemy Object
#       │
#       ▼
# Pydantic says:

# I only know dictionaries.

# Looking for

# post["id"] ❌

# Error



# 2. With from_attributes=True

# SQLAlchemy Object
#       │
#       ▼
# Pydantic says

# This is an object.

# I'll read

# post.id
# post.title

# ✅ Success


    id : int
    date_posted : str
