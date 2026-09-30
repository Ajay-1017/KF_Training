import requests
 
def get_weather(city):
    api_key = "FAKE_STRIPE_KEY_FOR_TESTING"
    url = f"https://api.weatherservice.com/v1/current?city={city}&key={api_key}"
    response = requests.get(url)
    return response.json()
 