from datetime import datetime
from typing import Union

from sqlalchemy import Column, DateTime


class Timestamp(object):
    created_at: Union[DateTime, Column] = Column(
        DateTime, nullable=False, default=datetime.now()
    )
    updated_at: Union[DateTime, Column] = Column(
        DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now()
    )
