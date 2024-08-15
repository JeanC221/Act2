from flask import Flask, redirect
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to our Docker Compose Project</h1>
    <ul>
        <li><a href="/c2">Ir al contenedor 2</a></li>
        <li><a href="/c3">Ir al contenedor 3 3</a></li>
    </ul>
    """

@app.route('/c2')
def redirect_to_cont2():
        response = requests.get('http://cont2:8000')
        response.raise_for_status()
        return response.text
    
@app.route('/c3')
def redirect_to_cont3():
        response = requests.get('http://cont3:8001')
        response.raise_for_status()
        return response.text
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)