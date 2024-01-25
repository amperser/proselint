"""Heroku web worker."""

import os

import redis
from rq import Connection
from rq import Queue
from rq import Worker

listen = ["high", "default", "low"]

redis_url = os.getenv("REDISTOGO_URL", "redis://localhost:6379")

conn = redis.from_url(redis_url)

if __name__ == "__main__":
    with Connection(conn):
        worker = Worker(list(map(Queue, listen)))
        worker.work()
