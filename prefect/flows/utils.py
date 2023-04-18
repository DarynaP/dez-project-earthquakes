import pandas as pd 
import numpy as np
import requests
import pycountry_convert as pc

def location(lat, long):
    """ Function that uses the latitude and longitude values 
    and gets the country, city, locality using Google maps API
    IMPORTANT: you need to get your API key
    https://developers.google.com/maps/get-started?hl=pt-br#enable-api-sdk
    """
    key = 'your_key_here'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={0},{1}&key={2}'.format(lat, long, key)
    r = requests.get(url)
    r_json = r.json()
    if len(r_json['results']) < 1: return None, None, None
    
    res = r_json['results'][0]['address_components']
    country  = next((c['long_name'] for c in res if 'country' in c['types']), None)
    city = next((c['long_name'] for c in res if 'administrative_area_level_1' in c['types']), None)
    locality = next((c['long_name'] for c in res if 'locality' in c['types']), None)
    return country, city, locality




def country_to_continent(country_name):
    """ Function that gets the continent using country name
    """
    try:
        country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    except KeyError:
        return None

    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name