from fastapi import FastAPI
from app.routes import blog_routes

app = FastAPI()
app.include_router(blog_routes.router, prefix="/api")  # Ensure this line is present
