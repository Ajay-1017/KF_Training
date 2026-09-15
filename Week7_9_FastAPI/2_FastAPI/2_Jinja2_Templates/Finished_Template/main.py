from fastapi import FastAPI , Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name = "static")

# Tell Jinja2 where the HTML templates are stored.
templates  = Jinja2Templates(directory="templates")

# Sample data that will be sent to the HTML template.
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


@app.get("/",include_in_schema=False , name = "home")
@app.get("/post",include_in_schema = False , name = "posts")
def home(request : Request):
    return templates.TemplateResponse(request,"home_finished.html",{"posts" : posts , "title": "home"})

    
