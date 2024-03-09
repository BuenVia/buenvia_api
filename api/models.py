from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    cat_eng = Column(String, unique=True, index=True)
    cat_spa = Column(String, index=True)

    words = relationship("Word", back_populates="vocab")


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True)
    word_eng = Column(String, index=True)
    word_spa = Column(String, index=True)
    cat_id = Column(Integer, ForeignKey("categories.id"))

    vocab = relationship("Category", back_populates="words")
