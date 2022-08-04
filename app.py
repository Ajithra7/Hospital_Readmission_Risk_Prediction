from flask import Flask,request, render_template
import pickle
import pandas as pd
import numpy as np
import os

PEOPLE_FOLDER = os.path.join('static', 'photo')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = PEOPLE_FOLDER

model = pickle.load(open("diabetes.pkl", "rb"))


@app.route('/')
def hello_world():
    return render_template("index.html")
@app.route('/index')
def show_index():
    full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
    return render_template("index.html", user_image = hospdischargeadmit.jpg)


@app.route('/predict',methods=['POST'])
def predict():
    text1 = request.form['1']
    text2 = request.form['2']
    text3 = request.form['3']
    text4 = request.form['4']
    text5 = request.form['5']
    text6 = request.form['6']
    text7 = request.form['7']
    text8 = request.form['8']
    text9 = request.form['9']
    text10 = request.form['10']
    text11 = request.form['11']
    text12 = request.form['12']
    text13 = request.form['13']
    text14 = request.form['14']
    text15=request.form['15']
    
    
    sample=[text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14,text15]      
    exp = np.array(sample).reshape(1,-1)
    output=model.predict(exp)
    output=output.item()
    
    #row_df = pd.DataFrame([pd.Series([text1,text2,text3,text4,text5,text6,text7])])
    #print(row_df)
    # output=model.predict(row_df)
    if output==1:
        return render_template('result.html', prediction_text="There is more chance for early redmission")
    else:
        return render_template('result.html', prediction_text="There is less chance for early readmission")
        

if __name__ == '__main__':
    app.run(port=5000)