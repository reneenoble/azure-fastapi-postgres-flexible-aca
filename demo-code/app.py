from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import models

app = FastAPI()
app.mount('/mount', StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def on_startup():
    models.create_db_and_tables()

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

# @app.get("/destinations")
# def destinations(destination=Destination):
#     all_destinations = models.Destination.objects.all()
#     return render(request, "destinations.html", {"destinations": all_destinations})


# @app.get("/destination/{pk}")
# class DestinationDetailView(generic.DetailView):
#     template_name = "destination_detail.html"
#     model = models.Destination
#     context_object_name = "destination"

# @app.get("/cruise/{pk}")
# class CruiseDetailView(generic.DetailView):
#     template_name = "cruise_detail.html"
#     model = models.Cruise
#     context_object_name = "cruise"

@app.get("/info_request", response_class=HTMLResponse)
class InfoRequestCreate():
    template_name = "info_request_create.html"
    model = models.InfoRequest
    fields = ["name", "email", "cruise", "notes"]
    success_url = reverse_lazy("index")
    success_message = "Thank you, %(name)s! We will email you when we have more information about %(cruise)s!"
