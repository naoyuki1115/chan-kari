from database.database import create_table
from fastapi import FastAPI
from router import item, user

# migrate table
create_table()

app = FastAPI()
app.include_router(user.router)
app.include_router(item.router)
