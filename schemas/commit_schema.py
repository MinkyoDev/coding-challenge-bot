from typing import Optional
from datetime import datetime

from pydantic import BaseModel

class CommitSchema(BaseModel):
    author: str
    level: Optional[str]
    title: Optional[str]
    url: str
    message: str
    commit_date: datetime