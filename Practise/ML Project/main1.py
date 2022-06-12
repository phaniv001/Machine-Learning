# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 23:22:55 2021

@author: laksh
"""

from flask import Flask, request, jsonify

app = Flask("MPG_Prediction")

#@app.route('/', methods=['Get'])

#def ping():
#    return "Ping Model Application!!! - Lakshman"


@app.route('/',methods = ['POST'])
def predict():
    vehicle_config = request.get_json()
    return vehicle_config


if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 5000)
