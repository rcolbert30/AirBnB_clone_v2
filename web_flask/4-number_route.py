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

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''
    Displays HBNB if successful
    '''
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
    replace underscore symbols with a space
    '''
    return "C {}".format(text.replace('_', ' '))

@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    '''
    Displays python, and text
    '''
    p = "Python {}".format(text)
    return p.replace('_', ' ')

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    '''
    Displays n only if it is a number
    '''
    return ('{} is a number'.format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
