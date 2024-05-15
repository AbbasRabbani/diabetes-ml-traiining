import json

import requests

input_data = {
  "pregnancies": 2,
  "Glucose": 100,
  "BloodPressure": 110,
  "SkinThickness": 8,
  "Insulin": 95,
  "BMI": 30,
  "DiabetesPedigreeFunction": 0.253,
  "Age": 30
}

url = "http://0.0.0.0/diabetes_prediction"

json_object = json.dumps(input_data)

response = requests.post(url, data=json_object)

print(response.text)
