import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'caloriesburned':181, 'stepcount':1524, 'weight_kg':66})

print(r.json())
