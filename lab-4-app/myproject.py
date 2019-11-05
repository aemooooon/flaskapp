from flask import Flask
from redis import Redis
import os

application = Flask(__name__)
redis = Redis(host="redis", port=6379)

@application.route('/')
def hello():
	redis.incr('hits')
	return 'Hello Docker Book reader! I have been seen {0} times'.format(redis.get('hits'))

if __name__ == "__main__":
	application.run(host="0.0.0.0", debug=True)
