from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis
redis_host = os.getenv("REDIS_HOST", "redis")
redis_port = int(os.getenv("REDIS_PORT", 6379))
r = redis.Redis(host=redis_host, port=redis_port, db=0)

@app.route('/')
def index():
    return "<h1>Welcome to the Flask + Redis App!</h1>"

@app.route('/count')
def count():
    count = r.incr('visits')  # Increment visit count
    return f"<h1>Visit count: {count}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
