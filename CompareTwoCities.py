import requests
import xml.etree.ElementTree as ET
import io
import Levenshtein

# http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=e7b5d6f4ca7d15baa039ec4528f9a68e&mode=xml
authKey = "e7b5d6f4ca7d15baa039ec4528f9a68e"
weatherApiUrl = "http://api.openweathermap.org/data/2.5/weather"
cityOne = "Katowice"
cityTwo = "Vienna"

print("FIRST EXAMPLE")
payloadOne = {'q': cityOne, 'APPID': authKey, 'mode': 'xml'}
resultOne = requests.get(weatherApiUrl, params=payloadOne)
print(resultOne.url)
print(resultOne.status_code)

treeOne = ET.parse(io.StringIO(resultOne.text))
rootOne = treeOne.getroot()

print(treeOne)
print(rootOne)
print(resultOne)
print(resultOne.text)

for child in rootOne:
    print(child.tag, child.attrib)
print("****")

print("SECOND EXAMPLE")
payloadTwo = {'q': cityTwo, 'APPID': authKey, 'mode': 'xml'}
resultTwo = requests.get(weatherApiUrl, params=payloadTwo)
print(resultTwo.url)
print(resultTwo.status_code)

treeTwo = ET.parse(io.StringIO(resultTwo.text))
rootTwo = treeTwo.getroot()

print(treeTwo)
print(rootTwo)
print(resultTwo)
print(resultTwo.text)
print("****")


print("****pywurlf****")
distTest = Levenshtein.distance("aa", "bb")
print(distTest)
distTwoWholeXMLs = Levenshtein.distance(resultOne.text, resultTwo.text)
print(distTwoWholeXMLs)
