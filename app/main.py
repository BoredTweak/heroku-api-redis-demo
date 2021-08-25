import threading
import redis
import sys
import time
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()
hostAddress = os.environ.get('REDIS_URL')
port = os.environ.get('REDIS_PORT')

app = FastAPI(root_path='/api')

@app.get('/heartbeat')
def get_heartbeat():
    r = redis.Redis(host=hostAddress, port=int(port))
    return r.get("heartbeat")

@app.post('/heartbeat')
def set_heartbeat():
    r = redis.Redis(host=hostAddress, port=int(port))
    r.set("heartbeat", time.time())
    return True

@app.get('/health')
def get_health():
    return f'{hostAddress} - {port}'
