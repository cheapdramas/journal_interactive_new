from fastapi import FastAPI
from routes import router as router
app = FastAPI()

app.include_router(router)
