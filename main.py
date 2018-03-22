from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import geoip
import configparser

app = Flask(__name__)

config = configparser.ConfigParser()  # Initialize configparser
config.read('config/config.ini')

# Config Data for the PostGre URI
user = config['POSTGRE']['User']
password = config['POSTGRE']['Password']
host = config['POSTGRE']['Host']
port = config['POSTGRE']['Port']
database = config['POSTGRE']['Database']

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:\\Users\\nconk\\PyCharmProjects\\IPGeoLocator\\test.db'
    #f'postgresql://{user}:{password}@{host}:{port}/{database}'
db = SQLAlchemy(app)


# Table class to create table when db.create_all() is called
class LocationData(db.Model):
    ip = db.Column(db.String, primary_key=True)

    def __repr__(self):
        return '<IP Address: {}'.format(self.ip)

    def get_data(self):
        ip_address = '216.246.161.55'
        city = geoip.get_city_lon_lat(ip_address)[0]
        country = geoip.get_country(ip_address)
        latitude = geoip.get_city_lon_lat(ip_address)[1]
        longitude = geoip.get_city_lon_lat(ip_address)[2]

        return {'ip': ip_address, 'city': city, 'country': country, 'latitude': latitude, 'longitude': longitude}

    @property
    def city(self):
        return self.get_data()['city']
    
    @property
    def country(self):
        return self.get_data()['country']
    
    @property
    def latitude(self):
        return self.get_data()['latitude']

    @property
    def longitude(self):
        return self.get_data()['longitude']

# Create the database and tables
db.create_all()

@app.route('/')
def welcome():
    return render_template('welcome.html'), 200


@app.route('/about')
def about():
    return render_template('about.html'), 200


@app.route('/index', methods = ['GET', 'POST'])
def index():
    user = LocationData(ip='216.246.161.55')
    data = LocationData.query.all()
    print(data)
    print(user.city)
    db.session.add(user)
    db.session.commit()
    return render_template('index.html', data = [user.country, user.city]), 200


if __name__ == '__main__':
    app.run(debug = True)
