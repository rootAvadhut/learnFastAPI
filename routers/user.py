from fastapi import APIRouter
from models.user import User

router = APIRouter()

@router.post("/users/")
async def create_user(user: User):
    return {
        "message": "User created successfully",
        "user": user
    }
