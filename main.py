from fastapi import FastAPI
from routes.route import article
app = FastAPI(   
    title="CCN API",
    description="This API performs the CRUD methods [GET,DELETE,POST,UPDATE] for the CCN News Feed",
    version="Wamolambo Lucky Ramasila",
    author="Wamolambo Lucky Ramasila")

app.include_router(article)
