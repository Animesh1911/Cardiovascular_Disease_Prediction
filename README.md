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
  <li>Glucose - (1 normal, 2 above normal, 3 well above normal)</li>![144010004-389dabb3-aecf-45b4-a057-245f90530a85](https://user-images.githubusercontent.com/71598356/144010279-9484e336-a56c-4228-a519-f2b3803a923a.png)

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
<strong>CORRELATIION PLOT BEFORE PREPROCESSING</strong><br>

![corr_before](https://user-images.githubusercontent.com/71598356/144009772-da974cd1-4c50-4d12-8614-b16a39b2017d.png)

The main causes of cardiovascular disease are high blood pressure, overweight, smoking and cholesterol.

From this correlation graph we can see that only age, weight and cholesterol are having some impact on the output variable. Also, blood pressure is not having any importance on the output. This is due to the presence of outliers.

We also know that cholesterol and glucose have 3 different levels. So we should also try to figure out which level affects the output the most.

<strong>OUTLIERS</strong><br>
There are many outliers present in Systolic BP, Diastolic BP, Height and Wieght columns.<br>
<table>
  <tr>
    <th>![sys](https://user-images.githubusercontent.com/71598356/144009934-2db89d66-3414-42a4-8482-e04dd33149fa.png)</th>
    <th>![dia](https://user-images.githubusercontent.com/71598356/144009921-ff94c3c9-d82f-4d3b-9c0c-3ba099e31121.png)</th>
  </tr>
  <tr>
    <th>![height](https://user-images.githubusercontent.com/71598356/144010004-389dabb3-aecf-45b4-a057-245f90530a85.png)</th>
    <th>![weight](https://user-images.githubusercontent.com/71598356/144009947-214a0258-5c61-4943-aab9-e40fa64ecbc6.png)</th>
  </tr>
</table>
<br>

<strong>
