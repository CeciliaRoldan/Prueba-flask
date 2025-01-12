# coding: cp1252 
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '¡Hola, mundo!'

@app.route('/my_function', methods=['POST'])
def my_function():
    data = request.json
    x = data['x']
    result = x * 2
    return jsonify({'result': result})

if __name__ == '__main__':
    #app.run(host='127.0.0.1', port=8000, debug=True)
    app.run()
