from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
loaded_model=pickle.load(open('regression_model.pkl', 'rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
   
    if request.method == "POST":
       
       year = request.form.get("year")
       month = request.form.get("month")
    print(year)
    df=pd.read_csv( 'real_'+ str(year)+ '.csv')

    my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
    my_prediction=my_prediction.tolist()
    
    if(int(month)==1):
       element = my_prediction[0:31]
    if(int(month)==2):
       element = my_prediction[31:59]
    if(int(month)==3):
       element = my_prediction[59:90]
    if(int(month)==4):
       element = my_prediction[90:120]
    if(int(month)==5):
       element = my_prediction[120:151]
    if(int(month)==6):
       element = my_prediction[151:181]
    if(int(month)==7):
       element = my_prediction[181:212]
    if(int(month)==8):
       element = my_prediction[212:243]
    if(int(month)==9):
       element = my_prediction[243:273]
    if(int(month)==10):
       element = my_prediction[273:303]
    if(int(month)==11):
       element = my_prediction[303:334]
    if(int(month)==12):
       element = my_prediction[334:365]
        
    return render_template('result.html',prediction = element)
if __name__ == '__main__':
	app.run(debug=True)