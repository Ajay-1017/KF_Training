from fastapi import FastAPI , Request
from fastapi.templating import Jinja2Templates


app = FastAPI()

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

@app.get("/",include_in_schema=False)
def home(request : Request):
       # Flow:
    #
    # 1. Browser sends a GET request for "/".
    #
    # 2. Uvicorn (ASGI server) receives the HTTP request
    #    and passes it to FastAPI.
    #
    # 3. FastAPI matches this request with @app.get("/").
    #
    # 4. FastAPI automatically creates a Request object
    #    that contains information about the current HTTP request
    #    (URL, method, headers, client, cookies, etc.).
    #
    # 5. FastAPI passes that Request object to this function
    #    through the parameter:
    #
    #           request: Request
    #
    #    We DO NOT create the Request object ourselves.
    #
    # 6. We pass the same Request object to Jinja2 using
    #    TemplateResponse().
    #
    # 7. Jinja2 uses:
    #       - request (current HTTP request)
    #       - home.html (template)
    #       - posts and title (context data)
    #    to render the final HTML page.
    #
    # 8. The rendered HTML is returned to Uvicorn,
    #    which sends it back to the browser.
    
    return templates.TemplateResponse(request,"home.html",{"posts" : posts , "title": "home"})

    
