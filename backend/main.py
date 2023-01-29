from database.database import engine
from model import Base

# migrate table
Base.metadata.create_all(engine)
