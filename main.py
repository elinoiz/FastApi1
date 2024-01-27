from fastapi import FastAPI


app = FastAPI()

@app.get('/')
async def start():
    return {"FIO" : "Gainullin Aleksandr Ruslanovich"}


@app.get('/users')
async def users():
    return {"number" : "89520321921"}

@app.get('/tools')
async def tools():
    return {"Tools" : "Python"}


    





