#importing libraries
from typing_extensions import TypedDict
from pydantic import BaseModel,Field

#define class
class Blog(BaseModel):
    title:str=Field(discription='title of the blog')
    content:str=Field(discription='The main content of the post blog')

class StateBlog(TypedDict):
    topic:str=Field(discription='The topic of the blog')
    blog:Blog=Field(discription='The blog objecy containing the title and content of blog')
    current_language:str=Field(discription='Current language of blog')
    
    