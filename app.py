from flask import Flask, request, redirect, url_for, flash, jsonify,render_template
import numpy as np
import pickle as p

from sklearn import preprocessing
import json


app = Flask(__name__)


@app.route('/', methods=['GET'])
def makecalc():
    if request.method == 'GET':
           modelfile = r'C:\Users\hnrne\Our_Trained_logistic_model.sav'
          # labelfile = r'C:\Users\hnrne\y.pickle'
          # scalerfile= r'C:\Users\hnrne\scaler.pickle'
         #  sc = p.load(open(scalerfile,'rb'))
          # y= p.load(open(labelfile , 'rb'))
          # y=list(y)
          # l=preprocessing.LabelEncoder().fit(y)
           model = p.load(open(modelfile, 'rb'))
           a= request.json['data']
           d = {'0': "hyperthyroid", '1': "hypothyroid", '2': "negative", '3': "sick"}

           prediction = np.array2string(model.predict(a))
           #print(prediction,type(prediction))
          # print(a,type(a))

           f=d.get(prediction[1])
           #print(f)
          # x= l.inverse_transform(prediction)
          # prediction = model.predict(y)
          #print(x)


  #  return jsonify(prediction)
    return jsonify(f)
@app.route('/predict')
def predict():
    return render_template('index.html')
@app.route('/predictOutput',methods=['POST'])
def output():
    if request.method == 'POST':
        f1 = float(request.form.get('t3measured'))
        f2 = float(request.form.get('t4u'))
        f3 = float(request.form.get('tumour'))
        f4 = float(request.form.get('tsh'))
        f5 = float(request.form.get('tt4measured'))
        f6 = float(request.form.get('age'))
        f7 = float(request.form.get('ftimeasured'))
        f8 = float(request.form.get('fti'))
        f9 = float(request.form.get('pregnant'))
        f10 = float(request.form.get('t4uu'))
        modelfile = r'C:\Users\hnrne\Our_Trained_logistic_model.sav'
        model = p.load(open(modelfile, 'rb'))
        d = {'0': "hyperthyroid", '1': "hypothyroid", '2': "negative", '3': "sick"}
        input_test = np.array([[f1,f2,f3,f4,f5,f6,f7,f8,f9,f10]])
        prediction = model.predict(input_test)
        print(prediction)
        f =d[str(prediction[0])]
        print(f)
    return render_template('index.html',output=f)






if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')