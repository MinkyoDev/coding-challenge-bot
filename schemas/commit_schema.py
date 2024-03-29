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

# tmp_data = {
#       "mid": "1",
#       "genre": "action",
#       "rate": 1.5,
#       "tag": None,
#       "date": "2024-01-30 16:37:42",
#       "some_variable_list": [1, 2]
# }

# tmp_movie = Movie(**tmp_data)
# print(tmp_movie)