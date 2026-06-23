from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import SessionLocal

from models.found_item import FoundItem

from schemas.found_item import FoundItemCreate

router = APIRouter(
    prefix="/found-items",
    tags=["Found Items"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_found_item(
    item: FoundItemCreate,
    db: Session = Depends(get_db)
):

    new_item = FoundItem(
        item_name=item.item_name,
        category=item.category,
        description=item.description,
        found_date=item.found_date,
        found_location=item.found_location,
        image_url=item.image_url,
        status=item.status
    )

    db.add(new_item)

    db.commit()

    db.refresh(new_item)

    return new_item


@router.get("/")
def get_found_items(
    status: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(FoundItem)

    if status:

        query = query.filter(
            FoundItem.status == status
        )

    return query.all()


@router.get("/{item_id}")
def get_found_item(
    item_id: int,
    db: Session = Depends(get_db)
):

    item = db.query(FoundItem).filter(
        FoundItem.id == item_id
    ).first()

    if not item:

        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item
