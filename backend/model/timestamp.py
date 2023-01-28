from sqlalchemy import Column, DateTime
from datetime import datetime


class Timestamp(object):
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(
        DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now()
    )
