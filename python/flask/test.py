#-*- coding: utf-8 -*-
'''
flask test
'''
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    '''
    hello word
    '''
    return 'Hello, World!'
if __name__ == '__main__':
    app.run()
    