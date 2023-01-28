from fastapi import FastAPI

from database.database import engine
from model import Base
from router import item, rental, user

# migrate table
Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(user.router)
app.include_router(item.router)
app.include_router(rental.router)
