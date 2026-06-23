from fastapi import APIRouter
from sqlalchemy.orm import Session

from database import SessionLocal

from models.lost_item import LostItem
from models.found_item import FoundItem
from models.claim import Claim
from services.matching_service import is_match

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.get("/total-lost-items")
def total_lost_items():

    db = SessionLocal()

    return {
        "total_lost_items":
        db.query(LostItem).count()
    }

@router.get("/total-found-items")
def total_found_items():

    db = SessionLocal()

    return {
        "total_found_items":
        db.query(FoundItem).count()
    }

@router.get("/successful-claims")
def successful_claims():

    db = SessionLocal()

    return {
        "successful_claims":
        db.query(Claim).filter(
            Claim.status == "Approved"
        ).count()
    }
  
@router.get("/matches")
def get_matches():

    db = SessionLocal()

    lost_items = db.query(LostItem).all()

    found_items = db.query(FoundItem).all()

    matches = []

    for lost in lost_items:

        for found in found_items:

            if is_match(lost, found):

                matches.append({
                    "lost_item": lost.item_name,
                    "found_item": found.item_name
                })

    return matches
