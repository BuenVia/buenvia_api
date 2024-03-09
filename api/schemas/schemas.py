from pydantic import BaseModel


class CategoryBase(BaseModel):
    cat_eng: str
    cat_spa: str


class CategoryModel(CategoryBase):
    id: int


class WordBase(BaseModel):
    word_eng: str
    word_spa: str
    cat_id: int


class WordModel(WordBase):
    id: int
