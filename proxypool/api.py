from flask import Flask, g
from proxypool.db import RedisClient

__all__ = ['app']
app = Flask(__name__)


def get_connection():
    if not hasattr(g, 'redis'):
        g.redis = RedisClient()
    return g.redis


@app.route('/')
def index():
    return '<h2>Welcome to Proxy Pool System</h2>'


@app.route('/random')
def get_proxy():
    connection = get_connection()
    return connection.random()


@app.route('/count')
def get_counts():
    connection = get_connection()
    return str(connection.count())


if __name__ == "__main__":
    app.run()
