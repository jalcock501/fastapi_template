""" ENDPOINTS FOR APIS """
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def root_get():
    "url root GET request"
    return{"title": "new project",
            "method": "GET"}

@router.post("/")
def root_post():
    "url root POST request"
    return{"title": "new project",
            "method": "POST"}
