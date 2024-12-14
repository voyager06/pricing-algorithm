import requests
from django.conf import settings

def get_competitors(lat, lng, radius=2000):
    headers = {"Authorization": f"Bearer {settings.YELP_API_KEY}"}
    url = "https://api.yelp.com/v3/businesses/search"
    params = {
        "term": "Indian Restaurant",
        "latitude": lat,
        "longitude": lng,
        "radius": radius,
        "sort_by": "rating",
        "limit": 5
    }
    response = requests.get(url, headers=headers, params=params).json()
    return response["businesses"]


def get_weather(lat, lng):
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {"lat": lat, "lon": lng, "appid": settings.WEATHER_API_KEY}
    response = requests.get(url, params=params).json()
    temp_kelvin = response['main']['temp']
    temp_fahrenheit = (temp_kelvin - 273.15) * 9/5 + 32
    rain = response.get('rain', {}).get('1h', 0)
    return {'temperature': temp_fahrenheit, 'rain': rain}


def adjust_prices(menu_items, weather, is_busy, competitors):
    adjusted_prices = {}
    for item in menu_items:
        lowest_price = min(
            [comp['menu'].get(item['name'], float('inf')) for comp in competitors]
        )
        if weather['temperature'] < 45 or weather['rain'] > 0.1 or is_busy:
            adjusted_prices[item['name']] = max(item['price'], lowest_price * 1.1)
        else:
            adjusted_prices[item['name']] = lowest_price
    return adjusted_prices

from sklearn.linear_model import LinearRegression

def train_model(menu_data, competitor_data, weather_data):
    X, y = [], []
    for comp in competitor_data:
        for item in comp['menu']:
            X.append([weather_data['temperature'], weather_data['rain']])
            y.append(item['price'])

    model = LinearRegression()
    model.fit(X, y)
    return model
