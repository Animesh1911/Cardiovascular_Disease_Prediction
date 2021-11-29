from flask import Flask, request, render_template
from flask_cors import cross_origin
import pickle
import xgboost as xgb
import numpy as np

app = Flask(__name__)

model = xgb.Booster()
model.load_model("xgb_model.bin")

sc = open('scaler.pkl','rb')
scaler = pickle.load(sc)

@app.route("/")
@cross_origin()
def home():
    return render_template('index.html')

@app.route("/predict", methods=["GET","POST"])
@cross_origin()
def predict():
    Gender = 0
    Chol_2 = 0
    Chol_3 = 0
    Gluc_2 = 0
    Gluc_3 = 0
    Smoke = 0
    Alco = 0
    Active = 0
    
    if request.method == 'POST':
        
        Age = request.form['Age']
        
        gender = request.form['Gender']
        if gender == 'Male':
            Gender = 1
        
        Height = request.form['Height']
        
        Weight = request.form['Weight']
        
        Sys_BP = request.form['Sys_bp']
        
        Dia_BP = request.form['Dia_bp']
        
        cholesterol = request.form['Chol_lvl']
        if cholesterol == "Level 2":
            Chol_2 = 1
        elif cholesterol == "Level 3":
            Chol_3 = 1
        
        glucose = request.form['Gluc_lvl']
        if glucose == "Level 2":
            Gluc_2 = 1
        elif glucose == "Level 3":
            Gluc_3 = 1
        
        smoker = request.form['Smoke']
        if smoker == 'Yes':
            Smoke = 1
            
        alchoholic = request.form['Alco']
        if alchoholic == 'Yes':
            Alco = 1
        
        activity = request.form['Active']
        if activity == 'Yes':
            Active = 1
            
        data = [
                Age, Gender, Height, Weight, Sys_BP, Dia_BP, Smoke,
                Alco, Active, Chol_2, Chol_3, Gluc_2, Gluc_3
                ]
        
        data = np.array(data).reshape((1,-1))
        
        data_scaled = scaler.transform(data)
        
        data_DM = xgb.DMatrix(data_scaled)
        
        cardio = model.predict(data_DM)
        output = round(cardio[0]*100,2)
        
        return render_template('index.html',prediction_text="Your chances of having Cardiovascular Disease is {} %.".format(output))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=False)