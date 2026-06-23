from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

from sqlalchemy.orm import Session

from database import SessionLocal

from models.lost_item import LostItem

from schemas.lost_item import LostItemCreate

router = APIRouter(
    prefix="/lost-items",
    tags=["Lost Items"]
)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@router.post("/")
def create_lost_item(
    item: LostItemCreate,
    db: Session = Depends(get_db)
):

    new_item = LostItem(
        item_name=item.item_name,
        category=item.category,
        description=item.description,
        lost_date=item.lost_date,
        lost_location=item.lost_location,
        image_url=item.image_url,
        status=item.status
    )

    db.add(new_item)

    db.commit()

    db.refresh(new_item)

    return new_item


@router.get("/")
def get_lost_items(
    category: str = None,
    db: Session = Depends(get_db)
):

    query = db.query(LostItem)

    if category:

        query = query.filter(
            LostItem.category == category
        )

    return query.all()


@router.get("/{item_id}")
def get_lost_item(
    item_id: int,
    db: Session = Depends(get_db)
):

    item = db.query(LostItem).filter(
        LostItem.id == item_id
    ).first()

    if not item:

        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    return item


@router.put("/{item_id}")
def update_lost_item(
    item_id: int,
    item: LostItemCreate,
    db: Session = Depends(get_db)
):

    db_item = db.query(LostItem).filter(
        LostItem.id == item_id
    ).first()

    if not db_item:

        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    db_item.item_name = item.item_name
    db_item.category = item.category
    db_item.description = item.description
    db_item.lost_date = item.lost_date
    db_item.lost_location = item.lost_location
    db_item.image_url = item.image_url
    db_item.status = item.status

    db.commit()

    return {
        "message":
        "Lost item updated"
    }


@router.delete("/{item_id}")
def delete_lost_item(
    item_id: int,
    db: Session = Depends(get_db)
):

    item = db.query(LostItem).filter(
        LostItem.id == item_id
    ).first()

    if not item:

        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

    db.delete(item)

    db.commit()

    return {
        "message":
        "Lost item deleted"
    }
