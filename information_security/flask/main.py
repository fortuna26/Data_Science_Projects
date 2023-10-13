#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"></ul></div>

# In[7]:


import pandas as pd
import pickle
from lightgbm import LGBMClassifier
from sklearn.preprocessing import StandardScaler

from flask import Flask, jsonify, request

# Load the model
with open('lgb_model.pkl', 'rb') as file: 
    model = pickle.load(file) 

# Init the app
app = Flask("default")


# Setup prediction endpoint
@app.route("/predict", methods=["POST"])
def predict():
    # Get the provided JSON
    X = request.get_json()
    # Perform a prediction
    preds = model.predict(pd.DataFrame(X, index=[0]))
    # Output json with prediction
    result = {"class label": preds[0]}
    return jsonify(result)


if __name__ == "__main__":
    # Run the app on local host and port 8989
    app.run(debug=True, host="0.0.0.0", port=8989)

