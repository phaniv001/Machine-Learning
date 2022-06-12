# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask, request, jsonify
from ml_model import predict_mpg
import pickle

app = Flask("MPG_Prediction")

@app.route('/',methods = ['POST'])
def predict():
    vehicle_config = request.get_json()
    with open('./model_bin', 'rb') as f_in:
        model = pickle.load(f_in)
        f_in.close()

    predictions = predict_mpg(vehicle_config, model) 
    response = {
        'mpg_predictions' : list(predictions)
        }
    return jsonify(response)


#@app.route('/', methods=['Get'])

#def ping():
#    return "Ping Model Application!!! - Lakshman"


if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 5000)

