# Name= Muhammad Fahad afroze, Email : fahadafroze99@gmail.com, Student ID: ECP-M-61637


"""We are making weather app, so first of all we need the api key, which will be used to requets the weather data. """

import requests  #First we need to fetch the API So i have to install the requets library to fetch the APi by using pip3 install requests 

api_key = '30d4741c779ba94c470ca1f63045390a' #This api key is taken from the openweathermap. to fetch the weather data. 

user_input = input("Enter city: ") #Now we have creacted the varaible to take city name from the user.  

#Now we will create a varialbe that will contain our requets meaning the data we will be fetching from the below URL. 
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")# I have searched a little bit for this URL.

"""Contains Userinput and api key to fetch the user city data. Now after running the code we were getting the code in 
jason and the data was very long, it containded other thing that we do not want. """

"""Now reducing the data to only temperaute and weather"""


weather = weather_data.json()['weather'][0]['main'] # Fetch weather data using index number from the weather data. 
temp = round(weather_data.json()['main']['temp']) # Fetch temp data from Json and used to round the number. 

print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp}ºF")

# After running the code we are getting the temp and weather of the city from the user. 

