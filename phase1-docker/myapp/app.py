from flask import Flask
import os 

app = Flask(__name__)

@app.route('/')
def home():
    name =os.environ.get('APP_NAME', 'My App')
    return f'<h1>{name}</h1><p>Running inside Docker!</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
