import requests

import pandas as pd

def get_lat_lon(city, country):
    
    filepath = "./data/worldcities.csv"
    world_cities = pd.read_csv(filepath)

    city_data = world_cities[(world_cities["country"] == country) &
                             (world_cities["city_ascii"] == city)]

    city_data = city_data.to_dict("records")

    if len(city_data) == 0:
        raise ValueError(f"{city}, {country} not found in {filepath}")

    latitude = city_data[0]["lat"]
    longitude = city_data[0]["lng"]

    return latitude, longitude

def get_rain_data(city, country, start_date, end_date):

    filepath = "./data/worldcities.csv"

    try:
        latitude, longitude = get_lat_lon(city, country)
    except ValueError as e:
        raise ValueError (f"No data available. {city}, {country} not found in {filepath}") from e

    base_historical_url = "https://archive-api.open-meteo.com/v1/archive?"
    params_lat_long = "latitude=" + str(latitude) + "&longitude=" + str(longitude)
    params_others = "&start_date=" + start_date + "&end_date=" + end_date + "&daily=precipitation_sum,rain_sum,precipitation_hours"
    
    final_url = base_historical_url + params_lat_long + params_others
    response = requests.get(final_url)
    
    print("Response Status Code:", response.status_code)
    
    if response.status_code !=200:
        raise ValueError (f"Error fetching data for {city}, {country}.")

    historical_rain_data = response.json()
    rain_data = historical_rain_data["daily"]

    return rain_data