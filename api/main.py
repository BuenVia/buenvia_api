from fastapi import FastAPI

from api.routers.category import router as category_router
from api.routers.word import router as word_router
app = FastAPI()


app.include_router(category_router)
app.include_router(word_router)


@app.get("/")
def index_route():
    return {"status": 200, "message": "index route"}


    