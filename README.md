# Cardiovascular_Disease_Prediction
An end to end ML model to predict whether a person has cardiovascular disease or not based on various features.

## Data
Dataset taken from Kaggle. Link - https://www.kaggle.com/sulianova/cardiovascular-disease-dataset

Total 70000 rows of data was present in the dataset.<br><br>
Independent Features: <br>
<ul>
  <li>Age (in days)</li>
  <li>Gender (1-Female, 2-Male)</li>
  <li>Height, Weight</li>
  <li>Systolic BP, Diastolic BP</li>
  <li>Cholesterol -  (1 normal, 2 above normal, 3 well above normal)</li>
  <li>Glucose - (1 normal, 2 above normal, 3 well above normal)</li>
  <li>Smoking, Alcohol intake, Physical activity</li>
</ul>  
<br>

Output Feature: Cardio<br>

## Preprocessing and EDA
<ul>
  <li>Converting Age values from no of days to years.
  <li>Plotting different graphs such as Boxplot, Histogram, Correlation Graph & Countplot to gather insights from the data.
  <li>Encoding the values of cholesterol and glucose to understand which level is having the highest impact on output.
  <li>Removing outliers from the data using IQR.
  <li>Applying StandardScaler to scale the data.
</ul>
<br>
<strong><u>CORRELATIION PLOT BEFORE PREPROCESSING</u></strong><br>

![corr_before](https://user-images.githubusercontent.com/71598356/144009772-da974cd1-4c50-4d12-8614-b16a39b2017d.png)

The main causes of cardiovascular disease are high blood pressure, overweight, smoking and cholesterol.

From this correlation graph we can see that only age, weight and cholesterol are having some impact on the output variable. Also, blood pressure is not having any importance on the output. This is due to the presence of outliers.

We also know that cholesterol and glucose have 3 different levels. So we should also try to figure out which level affects the output the most.

<strong><u>PLOTS</u></strong><br>
There are many outliers present in Systolic BP, Diastolic BP, Height and Wieght columns.<br>

![sys](https://user-images.githubusercontent.com/71598356/144012488-a125a2ab-829c-4c16-afb9-921f295474be.png)
![dia](https://user-images.githubusercontent.com/71598356/144012740-ba250169-5ee0-4777-b02c-99ef3ae80b24.png)

![h](https://user-images.githubusercontent.com/71598356/144014125-9c980d5e-aa4c-4df9-8dfe-8ebaecf683c2.png)
![w](https://user-images.githubusercontent.com/71598356/144014157-b981aee2-51e3-409d-9e66-dd2eac13d333.png)
 
Boxplots for Systolic BP, Diastolic BP, Height and Weight showing the outliers.
<br>
<br>

![gluc](https://user-images.githubusercontent.com/71598356/144014609-27e9afbe-b03e-4c23-87c2-e330ff019530.png)
![chol](https://user-images.githubusercontent.com/71598356/144014623-bf31ae9b-bb20-4b4b-b4ab-0e5129f0f890.png)

![gender](https://user-images.githubusercontent.com/71598356/144014680-e4025d7b-a07a-4037-b0f5-33c683bbc73c.png)
![smoke](https://user-images.githubusercontent.com/71598356/144014692-8ffab0f2-9cca-4b75-a788-f93531aa5cb0.png)
<br>
Some information obtained form the dataset.<br>
Percentage of male is 35.
Percentage of smoker is 9.
Percentage of alcoholic is 5.
Percentage of active people is 80.

We can see that as the levels of glucose and cholestrol are increases, the chances of having cardiovascular disease may increase.

<strong><u>CORRELATION PLOT AFTER OUTLIER REMOVAL</u></strong>
![corr_after](https://user-images.githubusercontent.com/71598356/144015234-209daeb0-c183-4407-80cf-922ef24934a7.png)
<br>
After the preprocessing, we can clearly see which feature contributes directly and indirectly to the output variable.

1.  Age, weight and level 3 cholesterol contribute positively to the output.
2.  Systolic BP and Diastolic BP contribute positively to the output.
3.  Level 1 cholesterol contribute negatively to the output.

Rest of the features do not have much effect on the output.

We can also note that each level of cholesterol is highly correlated to the corresponding same level of glucose. This means that if a person has level 3 cholesterol, the chance of him/her having level 3 glucose is high.
A similar case can be seen in systolic and diastolic BP which have a very high value of correlation.

Weight is also correlated to systolic and diastolic BP. Thus, if a person's weight increases his/her BP may also increase.

<br>

## Training and Testing

After preprocessing 61774 rows were left. Used a train-test split of 80:20.

5 different models were used for training and testing:
 - Logistic Regression
 - Random Forest
 - SVM
 - XGBoost
 - K Nearest Neighbours

(NOTE: The models are not yet optimized using Cross Validation. Will update soon).

Comparision of the 5 models :

![Accuracy](https://user-images.githubusercontent.com/71598356/144016128-3d4179be-2728-4a26-a856-56babe3322f9.png)

![Class 1 Recall](https://user-images.githubusercontent.com/71598356/144016150-ffc32335-e925-4bc6-9233-30cd2992171c.png)

![ROC vs  MODELS](https://user-images.githubusercontent.com/71598356/144016221-86655be0-775a-4513-96ba-d49af1e7dd24.png)

In medical classification, our main aim should be to reduce the number of false negative (class 1 recall should be high) because we do not want our model to predict a person who is having the disease (class 1) as not having the disease (class 0).

The XGBoost model outperforms all the other models in terms of accuracy as well as class 1 recall. Thus, we will use XGBoost model for deployment.

## Deployment
Saved the StandardScaler model and the XGBoost model for deployment.

Used Flask for the backend and HTML/CSS for the frontend.

As the user enters his data on our website, we store the data in a numpy array. We use our saved StandardScaler model for scaling down this data and then we pass this data to our model for making prediction.

The output is given as a percentage, which states that this much chance is there for the person to have the disease.

LINK - https://cardio-disease-prediction-api.herokuapp.com/
<br>

<strong>WEB APP</strong>
![app](https://user-images.githubusercontent.com/71598356/144017345-31ed3b51-df03-4b61-bea3-41c8d73805f1.jpeg)
