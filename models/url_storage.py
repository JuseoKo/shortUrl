from pydantic import BaseModel

class URLStorage(BaseModel):
    __tablename__ = "url_storage"
    original_url: str
    short_url: str