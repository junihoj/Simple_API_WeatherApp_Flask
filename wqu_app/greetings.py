import requests

def retrieve_ip_address():
    """return Ip address of the server"""
    response = requests.get('https://api.ipify.org')
    
    return response.text


def get_geolocation(ip_address):
    """return cord"""
    response = requests.get(f"https://ipinfo.io/{ip_address}").json()
#     print(response['loc'])
#     cords = response.json()['loc']
#     lat, lon = cords.split(',')
    return [float(coord) for coord in response['loc'].split(',')]


def get_weather(coords):
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    params = {'lat':coords[0], 'lon':coords[1]}
    response = requests.get(url, params=params, headers=headers)

    data = response.json()
    temperature = data['properties']['timeseries'][0]['data']['instant']['details']['air_temperature']
    
    return f"The temperature is {temperature}"


def greet(ip_address):
    #ip_address = retrieve_ip_address()
    coords = get_geolocation(ip_address)
    weather_data = get_weather(coords)
    
    return weather_data
    

# if __name__=='__main__':
#     greet(ip_address)