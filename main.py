from fastapi import FastAPI
from redis import Redis
import uvicorn

redis = Redis(host="redis",port=6379)
app = FastAPI()


@app.get("/")
def index():
    count = redis.incr("hits")
    return {"message":"Welcome to FastAPI Server","hits":count}


if __name__=='__main__':
    uvicorn.run('main:app',port=80,host='0.0.0.0')

