from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import (
    Base,
    engine
)

from models.user import User
from models.lost_item import LostItem
from models.found_item import FoundItem
from models.claim import Claim

from routes.auth import router as auth_router
from routes.lost_items import router as lost_router
from routes.found_items import router as found_router
from routes.claims import router as claim_router
from routes.reports import router as report_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Lost & Found Management System"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(lost_router)
app.include_router(found_router)
app.include_router(claim_router)
app.include_router(report_router)


@app.get("/")
def home():

    return {
        "message":
        "Lost & Found Management System"
    }
