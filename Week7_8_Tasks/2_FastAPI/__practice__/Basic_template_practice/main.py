
from fastapi import FastAPI , Request
from fastapi.templating import Jinja2Templates

templates  = Jinja2Templates(directory= "templates")

app = FastAPI() # our web app (object)

posts : list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025",
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025",
    },
]

@app.get("/home")
def home():
    return {"message" : "hiii!"}

@app.get("/posts")
@app.get("/")
def home(request : Request):
    return templates.TemplateResponse(
                request , 
                "home.html",
                {
                    "title" : "home",
                    "posts" : posts
                }
      
    )

@app.get("/api/posts")
def get_posts():
    return posts


