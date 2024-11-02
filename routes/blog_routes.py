from fastapi import APIRouter, HTTPException
from app.models import Blog
from app.database import db

router = APIRouter()

@router.post("/blog")  # This should correspond to the POST request
async def create_blog(blog: Blog):
    blog_dict = blog.dict()
    result = await db["blogs"].insert_one(blog_dict)
    return {"id": str(result.inserted_id)}

@router.get("/blogs")  # This should correspond to the GET request
async def list_blogs():
    blogs = await db["blogs"].find().to_list(100)
    return blogs
