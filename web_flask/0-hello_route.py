#!/usr/bin/python3
'''
starts Flask
listen: 0.0.00, port 5000
'''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb_hello():
    '''
    display hello if works
    '''
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
