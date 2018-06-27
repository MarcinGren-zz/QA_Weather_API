import requests

# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=e7b5d6f4ca7d15baa039ec4528f9a68e&mode=xml
authKey = "e7b5d6f4ca7d15baa039ec4528f9a68e"
weatherApiUrl = "http://api.openweathermap.org/data/2.5/weather"
cityList = ['Katowice', 'London', 'Vienna', 'Glasgow', 'Beijing', 'asdzxc']
results = []

for i in range(len(cityList)):
    payload = {'q': cityList[i], 'APPID': authKey, 'mode': 'xml'}
    r = requests.get(weatherApiUrl, params=payload)
    print(r.url)
    print(r.status_code)
    results.append(r.status_code)

successfulRequests = [i for i, x in enumerate(results) if x == 200]
unsuccessfulRequests = [i for i, x in enumerate(results) if x == 404]
print("200: " + str(len(successfulRequests)) + " 404: " + str(len(unsuccessfulRequests)) + " Total: "
      + str(len(successfulRequests) + len(unsuccessfulRequests)))
