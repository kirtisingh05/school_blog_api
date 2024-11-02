from pydantic import BaseModel, Field
from typing import Optional

class Blog(BaseModel):
    title: str = Field("My First Blog")
    content: str = Field("This is the content of the blog.")
    author: Optional[str] = "Kirti Singh"
