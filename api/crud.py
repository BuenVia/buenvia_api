from sqlalchemy.orm import Session

from . import models
from .schemas import schemas


def read_categories(db: Session):
    return db.query(models.Category).all()


def read_single_category(db: Session, cat_id):
    db_cat = db.query(models.Category).get(cat_id)
    return db_cat


def create_category(db: Session, cat_eng, cat_spa):
    db_cat = models.Category(cat_eng=cat_eng, cat_spa=cat_spa)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat


def create_category_bulk(db: Session, categories: list[schemas.CategoryBase]):
    db_cats = models.Category()
    # db.add(db_cats)
    # db.commit()
    # db.refresh(db_cats)
    return db_cats


def update_category(db: Session, category, cat_id):
    db_cat = db.query(models.Category).get(cat_id)
    db_cat.cat_eng = category.cat_eng
    db_cat.cat_spa = category.cat_spa
    db.commit()
    db.refresh(db_cat)
    return db_cat


def delete_category(db: Session, cat_id):
    cat = db.query(models.Category).get(cat_id)
    db.delete(cat)
    db.commit()


def read_words(db: Session):
    pass


def get_single_word(db: Session):
    pass


def create_word(db: Session):
    pass


def update_word(db: Session):
    pass


def delete_word(db: Session):
    pass
