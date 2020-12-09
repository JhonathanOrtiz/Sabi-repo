from pydantic import BaseModel
from typing import Optional

class Query(BaseModel):
    text: str
    audio: Optional[bytes] = None
    session_id: Optional[str] = None


