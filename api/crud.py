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
    for cats in categories:
        db.add(models.Category(cat_eng=cats.cat_eng, cat_spa=cats.cat_spa))
    db.commit()
    return "done"


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
    return db.query(models.Word).all()


def get_single_word(db: Session):
    pass


def create_word(db: Session, word_eng, word_spa, cat_id):
    db_cat = models.Word(word_eng=word_eng, word_spa=word_spa, cat_id=cat_id)
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def create_words_bulk(db: Session, words: list[schemas.WordBase]):
    for word in words:
        db.add(models.Word(word_eng=word.word_eng, word_spa=word.word_spa, cat_id=word.cat_id))
    db.commit()
    return "done"


def update_word(db: Session):
    pass


def delete_word(db: Session):
    pass


def get_words_category(db: Session, cat_id):
    result = db.query(models.Category).join(models.Word).filter(models.Word.cat_id == cat_id).all()
    for row in result:
        for word in row.words:
            continue
            
    return result
