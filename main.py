from flask import Flask, render_template
import models
import geoip
import configparser

app = Flask(__name__)

configuration = configparser.ConfigParser()  # Initialize configparser
configuration.read('config/config.ini')

sqlite_location = configuration['SQLITE']['Location']


@app.route('/')
def welcome():
    return render_template('welcome.html')


@app.route('/index', methods = ['POST'])
def index():
    models.create_connection(sqlite_location)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
