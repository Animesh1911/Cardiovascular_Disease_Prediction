#loading models
import pickle
import xgboost as xgb
import numpy as np

model = xgb.Booster()
model.load_model("xgb_model.bin")

sc = open('scaler.pkl','rb')
scaler = pickle.load(sc)

#%%

#user input
Age = int(input())
Gender = int(input())
Height = int(input())
Weight = int(input())
Sys_BP = int(input())
Dia_BP = int(input())
Chol_lvl = int(input())
Gluc_lvl = int(input())
Smoke = int(input())
Alco = int(input())
Active = int(input())

Chol_2 = 0
Chol_3 = 0
Gluc_2 = 0
Gluc_3 = 0

if Chol_lvl == 2:
    Chol_2 = 1
elif Chol_lvl == 3:
    Chol_3 = 1
    
if Gluc_lvl == 2:
    Gluc_2 = 1
elif Gluc_lvl == 3:
    Gluc_3 = 1
    
data = [
    Age, Gender, Height, Weight, Sys_BP, Dia_BP, Smoke,
    Alco, Active, Chol_2, Chol_3, Gluc_2, Gluc_3
    ]

data = np.array(data).reshape((1,-1))

#%%
data_scaled = scaler.transform(data)
#%%
data_DM = xgb.DMatrix(data_scaled)

#%% 
cardio = model.predict(data_DM)
output = round(cardio[0]*100,4)