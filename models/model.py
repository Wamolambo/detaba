from pydantic import BaseModel

# dataset model
class Article(BaseModel):
    paragraph: str
    title: str
    author: str
    url: str