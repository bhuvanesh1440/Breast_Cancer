import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import xlrd as rxl
import xlsxwriter as wxl

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

def get_row():
    wb=rxl.open_workbook('test.xlsx')
    sheet=wb.sheet_by_index(0)
    row_count=sheet.nrows
    return row_count

@app.route('/')
def home():
    
    return render_template('h.html')
@app.route('/detect')
def detect():
    return render_template('d.html')
@app.route('/riskpred')
def riskpred():
    return render_template('r.html')



@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features=[]
    ct=request.form['ct']
    int_features.append(int(ct))
    ucsize=request.form['ucsize']
    int_features.append(int(ucsize))
    ucshape=request.form['ucshape']
    int_features.append(int(ucshape))
    ma=request.form['ma']
    int_features.append(int(ma))
    secs=request.form['secs']
    int_features.append(int(secs))
    bn=request.form['bn']
    int_features.append(int(bn))
    bc=request.form['bc']
    int_features.append(int(bc))
    nn=request.form['nn']
    int_features.append(int(nn))
    mi=request.form['mi']
    int_features.append(int(mi))
    print(int_features)
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = prediction

    if int(output)==2:
        return render_template('d.html', prediction_text='Result : Benign Tumor')
    else:
        return render_template('d.html', prediction_text='Result : Malignant Tumor')

if __name__ == "__main__":
    app.run(debug=True)