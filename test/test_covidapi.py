import requests

response = requests.get("https://coronavirus-tracker-api.herokuapp.com/v2/locations?country_code=MU")

outputjson = response.json() 
#print (outputjson)
print ("Confirmed cases : " + str(outputjson['latest']['confirmed']))
print ("Death: " + str(outputjson['latest']['deaths']))
print ("Recovered: " + str(outputjson['latest']['recovered']))


