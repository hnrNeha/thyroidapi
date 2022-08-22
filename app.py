from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
from sklearn import preprocessing
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def makecalc():
    if request.method == 'GET':
           modelfile = r'C:\Users\hnrne\Our_Trained_logistic_model.sav'
          # labelfile= r'C:\Users\hnrne\l.pickle'
          # scalerfile= r'C:\Users\hnrne\scaler.pickle'
         #  sc = p.load(open(scalerfile,'rb'))
           #l= p.load(open(labelfile,'rb'))
           model = p.load(open(modelfile, 'rb'))
           a= request.json['data']
           d = {0: "hyperthyroid", 1: "hypothyroid", 2: "negative", 3: "sick"}
           #j_data =list(json.dumps(b))
          # y=sc.fit_transform(b)


           prediction = model.predict(np.array([a]))
           print(prediction,type(prediction))
           print(a,type(a))

          # f=d[prediction[0]]
          # print(f)
          # x= l.inverse_transform(prediction)
          # prediction = model.predict(y)


    return jsonify(prediction)

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')