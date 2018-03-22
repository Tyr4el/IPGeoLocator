import geoip2.database
import configparser
from flask import request

configuration = configparser.ConfigParser()  # Initialize configparser
configuration.read('config/config.ini')

city_database_location = configuration['MAXMIND']['CityDatabaseLocation']
country_database_location = configuration['MAXMIND']['CountryDatabaseLocation']

reader_city = geoip2.database.Reader(city_database_location)
reader_country = geoip2.database.Reader(country_database_location)


def get_ip_address():
    return request.remote_addr


def get_city_lon_lat(ip):
    response = reader_city.city(ip)

    city_name = response.city.name
    latitude = response.location.latitude
    longitude = response.location.longitude

    return city_name, latitude, longitude


def get_country(ip):
    response = reader_country.country(ip)

    country_name = response.country.name

    return country_name

