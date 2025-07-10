from pydantic import BaseModel

class Notification(BaseModel):
    Type: str
    Name: str
    Description: str

