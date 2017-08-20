from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='0.0.0.0', port=6379)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def counter(path):
  if not redis.exists(path):
    redis.set(path, 1)
    redis.expire(path, 300)
  else:
    redis.incr(path)
  
  return redis.get(path)

if __name__ ==  "__main__":
  app.run(host="0.0.0.0", port=3000, debug=True)
