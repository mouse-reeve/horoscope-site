''' a generative horoscope site '''
from flask import Flask, render_template
from horoscope_generator import HoroscopeGenerator
import json
import random

# Config
app = Flask(__name__)


# ROUTES
@app.route('/')
def index():
    ''' render the basic template for angular '''
    return render_template('index.html', data=horoscope_data())


@app.route('/api/horoscope', methods=['GET'])
def get_horoscope():
    ''' return horoscope data to client '''
    return json.dumps(horoscope_data())


def horoscope_data():
    ''' Get a generated horoscope '''
    animals = ['hermit crab', 'puppy', 'seagull', 'sea slug']
    icons = [
        u'\u263C', # sun
        u'\u2694', # swords
        u'\u2696', # scales
        u'\u00F8', # o slash
        u'\u2741', # flower
        u'\u26B1', # urn
        u'\u269A', # staff of hermes
        u'\u27E1', # concave diamond
        u'\u2932', # crosses arrows
    ]

    horoscope = HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence())

    options = [str(i) for i in range(0, 9)] + ['A', 'B', 'C', 'D', 'E', 'F']
    color = [random.choice(options) for _ in range(6)]
    return {
        'horoscope': horoscope,
        'animal': random.choice(animals),
        'icon': random.choice(icons),
        'color': ''.join(color)
    }


if __name__ == '__main__':
    app.debug = True
    app.run(port=4000)

