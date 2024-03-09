from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, models
from ..schemas import schemas
from ..database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/categories/all", response_model=list[schemas.CategoryModel])
def get_categories(db: Session = Depends(get_db)):
    categories = crud.read_categories(db)
    if len(categories) == 0:
        raise HTTPException(status_code=404, detail="No results in table")
    return categories


@router.get("/categories/{cat_id}", response_model=schemas.CategoryModel)
def get_single_category(cat_id, db: Session = Depends(get_db)):
    category = crud.read_single_category(cat_id=cat_id, db=db)
    if not category:
        raise HTTPException(status_code=404, detail="Nothing to return")
    return category


@router.post("/categories")
def post_category(category: schemas.CategoryBase, db: Session = Depends(get_db)):
    return crud.create_category(db=db, cat_eng=category.cat_eng, cat_spa=category.cat_spa)


@router.post("/categories/bulk")
def post_category_bulk(categories: list[schemas.CategoryBase], db: Session = Depends(get_db)):
    bulk_import = crud.create_category_bulk(categories=categories, db=db)
    return bulk_import


@router.put("/categories/{cat_id}")
def put_category(cat_id, category: schemas.CategoryModel, db: Session = Depends(get_db)):
    category = crud.update_category(cat_id=cat_id, category=category, db=db)
    return category


@router.delete("/categories/{cat_id}")
def delete_category(cat_id, db: Session = Depends(get_db)):
    try:
        crud.delete_category(cat_id=cat_id, db=db)
        return f"Deleted {cat_id}"
    except Exception:
        raise HTTPException(status_code=404, detail="Category doesn't exist")
