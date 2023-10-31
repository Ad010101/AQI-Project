# from flask import Flask,render_template,url_for,request
# import pandas as pd 
# import pickle
# loaded_model=pickle.load(open('regression_model.pkl', 'rb'))
# app = Flask(__name__)

# @app.route('/')
# def home():
# 	return render_template('home.html')

# @app.route('/predict',methods=['POST','GET'])
# def predict():
   
#     if request.method == "POST":
       
#        year = request.form.get("year")
#        month = request.form.get("month")
#     print(year)
#     df=pd.read_csv( 'real_'+ str(year)+ '.csv')

#     my_prediction=loaded_model.predict(df.iloc[:,:-1].values)
#     my_prediction=my_prediction.tolist()
#     month = int(month)  # Assuming you already have the month and year defined
#     day_ranges = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 303, 334]
#     if(year!=2016):
#         month = int(month)  # Assuming you already have the month and year defined

#         days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#         if 1 <= month <= 12:
#             start_day = sum(days_in_month[:month])
#             end_day = start_day + days_in_month[month]

#             if year != 2016:
#                 if month == 2:
#                     start_day += 1  # Adjust for leap year
#                     end_day += 1

#             element = my_prediction[start_day:end_day]
#         else:
#             print("Invalid month")
#     else:
#         days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#         if 1 <= month <= 12:
#             start_day = sum(days_in_month[:month])
#             end_day = start_day + days_in_month[month]

#             if year == 2016 and month == 2:
                
#                 end_day += 1

#             element = my_prediction[start_day:end_day]


#     return render_template('result.html',prediction = element)
# if __name__ == '__main__':
# 	app.run(debug=True)
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

    my_prediction = loaded_model.predict(df.iloc[:, :-1].values)
    my_prediction = my_prediction.tolist()
    month = int(month)  # Assuming you already have the month and year defined

        # Rest of your code...

        # Convert negative predictions to positive
    my_prediction = [abs(value) for value in my_prediction]

    
    month = int(month)  # Assuming you already have the month and year defined
    day_ranges = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 303, 334]
    if(year!=2016):
        month = int(month)  # Assuming you already have the month and year defined

        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if 1 <= month <= 12:
            start_day = sum(days_in_month[:month])
            end_day = start_day + days_in_month[month]

            if year != 2016:
                if month == 2:
                    start_day += 1  # Adjust for leap year
                    end_day += 1

            element = my_prediction[start_day:end_day]
        else:
            print("Invalid month")
    else:
        days_in_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        if 1 <= month <= 12:
            start_day = sum(days_in_month[:month])
            end_day = start_day + days_in_month[month]

            if year == 2016 and month == 2:
                
                end_day += 1

            element = my_prediction[start_day:end_day]

    return render_template('result.html',prediction = element)
if __name__ == '__main__':
	app.run(debug=True)
