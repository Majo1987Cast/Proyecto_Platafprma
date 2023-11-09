from flask import Flask, render_template
import requests
from dotenv import load_dotenv, dotenv_values

config = dotenv_values('.env')


app = Flask(__name__)

def get_weather_data(city):
    API_KEY = config['API_KEY']
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang=es&units=metric&appid={API_KEY}'
    r = requests.get(url).json()
    print(r)
    return r 


@app.route('/about')
def about():
    get_weather_data('Guayaquil')
    return get_weather_data('Guayaquil')

@app.route('/clima')
def clima():
    return 'Obtener todo la información del clima'


if __name__ == '__main__':
    app.run(debug=True)

