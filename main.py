from fastapi import FastAPI
from routers import user

app = FastAPI()

# Register API routers
app.include_router(user.router)

