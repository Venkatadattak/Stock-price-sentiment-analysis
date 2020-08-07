from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('stockRF.pickle', 'rb'))
countvector = pickle.load(open('vectorizer.pickle','rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/classify", methods=['POST'])
def classify():
  if request.method == 'POST':  
      head1=request.form['head1']
      head2=request.form['head2']
      head3=request.form['head3']
      head4=request.form['head4']
      head5=request.form['head5']
      head6=request.form['head6']
      head7=request.form['head7']
      head8=request.form['head8']
      head9=request.form['head9']
      head10=request.form['head10']
      head11=request.form['head11']
      head12=request.form['head12']
      head13=request.form['head13']
      head14=request.form['head14']
      head15=request.form['head15']
      head16=request.form['head16']
      head17=request.form['head17']
      head18=request.form['head18']
      head19=request.form['head19']
      head20=request.form['head20']
      head21=request.form['head21']
      head22=request.form['head22']
      head23=request.form['head23']
      head24=request.form['head24']
      head25=request.form['head25']
      
      data=head1+" "+head2+" "+head3+" "+head4+" "+head5+" "+head6+" "+head7+" "+head8+" "+head9+" "+head10+" "+head11+" "+head12+" "+head13+" "+head14+" "+head15+" "+head16+" "+head17+" "+head18+" "+head19+" "+head20+" "+head21+" "+head22+" "+head23+" "+head24+" "+head25
      data=data.lower()
      
      cdata=countvector.transform([data])
      
      prediction=model.predict(cdata)
      output=prediction[0]
      
      if output==0:
        return render_template('classify.html',prediction_text=" Dont Invest {}".format(output))
      else:
        return render_template('classify.html',prediction_text="Yes you can Invest {}".format(output))  
  else:
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
