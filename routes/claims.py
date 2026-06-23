from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    BackgroundTasks
)

from sqlalchemy.orm import Session

from database import SessionLocal

from models.claim import Claim
from models.found_item import FoundItem

router = APIRouter(
    prefix="/claims",
    tags=["Claims"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


def send_email():

    print("Claim approved email sent")


@router.post("/{found_item_id}")
def create_claim(
    found_item_id: int,
    user_id: int,
    db: Session = Depends(get_db)
):

    item = db.query(FoundItem).filter(
        FoundItem.id == found_item_id
    ).first()

    if not item:

        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    claim = Claim(
        found_item_id=found_item_id,
        user_id=user_id,
        status="Pending"
    )

    db.add(claim)

    db.commit()

    return {
        "message":
        "Claim submitted"
    }


@router.get("/")
def get_claims(
    status: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(Claim)

    if status:

        query = query.filter(
            Claim.status == status
        )

    return query.all()


@router.put("/{claim_id}/approve")
def approve_claim(
    claim_id: int,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db)
):

    claim = db.query(Claim).filter(
        Claim.id == claim_id
    ).first()

    if not claim:

        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    existing = db.query(Claim).filter(
        Claim.found_item_id == claim.found_item_id,
        Claim.status == "Approved"
    ).first()

    if existing:

        raise HTTPException(
            status_code=400,
            detail="Item already claimed"
        )

    claim.status = "Approved"

    item = db.query(FoundItem).filter(
        FoundItem.id == claim.found_item_id
    ).first()

    item.status = "Claimed"

    db.commit()

    background_tasks.add_task(
        send_email
    )

    return {
        "message":
        "Claim approved"
    }


@router.put("/{claim_id}/reject")
def reject_claim(
    claim_id: int,
    db: Session = Depends(get_db)
):

    claim = db.query(Claim).filter(
        Claim.id == claim_id
    ).first()

    if not claim:

        raise HTTPException(
            status_code=404,
            detail="Claim not found"
        )

    claim.status = "Rejected"

    db.commit()

    return {
        "message":
        "Claim rejected"
    }
