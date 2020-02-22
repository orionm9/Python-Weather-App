import requests


def weather_data(query, mtype):
    res = requests.get('http://api.openweathermap.org/data/2.5/weather?' + query + '&APPID=7615996b696e84054c46d1ec9fc6a4b6&units=' + mtype)
    return res.json()


def print_weather(result, city):
    print("{}'s Temperature: {}°F ".format(city, result['main']['temp']))
    print("{}'s High Temp: {}°F".format(city, result['main']['temp_max']))
    print("{}'s Low Temp: {}°F".format(city, result['main']['temp_min']))
    print("Wind speed: {} miles/second".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))


def print_metric(result, city):
    print("{}'s Temperature: {}°C ".format(city, result['main']['temp']))
    print("{}'s High Temp: {}°C".format(city, result['main']['temp_max']))
    print("{}'s Low Temp: {}°C".format(city, result['main']['temp_min']))
    print("Wind speed: {} meters/second".format(result['wind']['speed']))
    print("Description: {}".format(result['weather'][0]['description']))
    print("Weather: {}".format(result['weather'][0]['main']))


def main():
    city = input('Enter the city:')
    mtype = input('Do you want Imperial or Metric?').lower().strip()
    print()
    try:
        query = 'q=' + city
        w_data = weather_data(query, mtype)
        if mtype == "imperial":
            print_weather(w_data, city)
        elif mtype == "metric":
            print_metric(w_data, city)
        print()
    except:
        print('Sorry, that city name is not found...')


if __name__ == '__main__':
    main()
