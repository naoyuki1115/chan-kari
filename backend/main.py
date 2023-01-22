from fastapi import FastAPI
from router import profile, item

app = FastAPI()
app.include_router(item.router)
