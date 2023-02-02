from datetime import datetime

from sqlalchemy import Column, DateTime


class Timestamp(object):
    created_at: DateTime = Column(
        DateTime, nullable=False, default=datetime.now()
    )  # type:ignore
    updated_at: DateTime = Column(
        DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now()
    )  # type:ignore
