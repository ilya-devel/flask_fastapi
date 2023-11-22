import uvicorn
from fastapi import FastAPI, HTTPException
import logging
from pydantic import BaseModel
from typing import Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


class Genre(BaseModel):
    id: int
    name: str


class Movie(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    genre: Genre


movies = [
    Movie(id=0, title='Movie 1', description='', genre=Genre(id=0, name='horror')),
    Movie(id=0, title='Movie 1', description='', genre=Genre(id=0, name='horror')),
    Movie(id=0, title='Movie 1', description='', genre=Genre(id=1, name='comedy')),
    Movie(id=0, title='Movie 1', description='', genre=Genre(id=0, name='horror')),
    Movie(id=0, title='Movie 1', description='', genre=Genre(id=2, name='drama')),
    Movie(id=0, title='Movie 1', description='', genre=Genre(id=0, name='horror')),
]


@app.get('/movies/', response_model=list[Movie])
async def get_movies(genre_id: int = None, genre_name=None):
    if genre_id is not None:
        return [movie for movie in movies if movie.genre.id == genre_id]
    if genre_name is not None:
        return [movie for movie in movies if movie.genre.name == genre_name]
    return movies


if __name__ == '__main__':
    uvicorn.run("task_2:app", host='localhost', port=8000, reload=True)
