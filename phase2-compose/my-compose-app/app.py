from flask import Flask
import os
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    db_host = os.environ.get('DB_HOST', 'localhost')
    return f'<h1>Flask + PostgreSQL</h1><p>Connected to database at: {db_host}</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
