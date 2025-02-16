
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    firstName: Optional[str] = None
    lastName: Optional[str] = None