from fastapi import FastAPI
from routers import lab_routes,img_routes

app=FastAPI()

@app.get('/')
def home():
    return {"message":"Welcome to Medisense Website"}


app.include_router(router=lab_routes.router)

app.include_router(router=img_routes.router)