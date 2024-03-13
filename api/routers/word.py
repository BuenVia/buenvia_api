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


@router.get("/words/all", response_model=list[schemas.WordModel])
def get_all_words(db: Session = Depends(get_db)):
    words = crud.read_words(db)
    if len (words) == 0:
        raise HTTPException(status_code=404, detail="Nothing to return")
    return words


@router.post("/words", response_model=schemas.WordModel)
def post_single_word(word: schemas.WordBase, db: Session = Depends(get_db)):
    return crud.create_word(db=db, word_eng=word.word_eng, word_spa=word.word_spa, cat_id=word.cat_id)


@router.post("/words/bulk")
def post_word_bulk(words: list[schemas.WordBase], db: Session = Depends(get_db)):
    bulk_import = crud.create_words_bulk(words=words, db=db)
    return bulk_import