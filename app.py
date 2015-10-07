''' a generative horoscope site '''
import base64
from flask import Flask, render_template
from horoscope_generator import HoroscopeGenerator
import random

# Config
app = Flask(__name__)

icons = {
    'sun': u'\u2609',
    'mercury': u'\u263F',
    'swords': u'\u2694',
    'aesculapius': u'\u2695',
    'hermes': u'\u269A',
    'star': u'\u2727',
    'scales': u'\u2696',
    'oslash': u'\u00F8',
    '2circles': u'\u260D',
    'flower': u'\u2741',
    'urn': u'\u26B1',
    'concavediamond': u'\u27E1',
    'crossedarrows': u'\u2932',
    'uparrows': u'\u2949',
    'tetragram': u'\u2635',
    'dharma': u'\u2638',
    'saturn': u'\u2644',
    'uranus': u'\u2645',
    'neptune': u'\u2646',
    'infinity': u'\u221E',
    'footnote': u'\u2021',
    'diamond': u'\u25C7',
}

# ROUTES
@app.route('/')
def index():
    ''' render the basic template for angular '''
    return render_template('index.html', data=horoscope_data())


@app.route('/<uid>', methods=['GET'])
def load_fortune(uid):
    ''' display a specific fortune from uid '''
    content = base64.b64decode(uid)
    items = content.split('|')
    data = {
        'horoscope': items[0],
        'animal': items[1],
        'icon': icons[items[2]],
        'color': items[3]
    }
    return render_template('index.html', data=data)


def horoscope_data():
    ''' Get a generated horoscope '''
    animals = [
        'hermit crab',
        'puppy',
        'seagull',
        'sea slug',
        'giraffe',
        'pigeon',
        'gnat',
        'armadillo',
        'nutria',
        'alligator',
        'blobfish',
        'earthworm'
    ]


    horoscope = HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence())
    animal = random.choice(animals)
    icon = random.choice(icons.keys())
    options = [str(i) for i in range(0, 9)] + ['A', 'B', 'C', 'D', 'E', 'F']
    color = ''.join([random.choice(options) for _ in range(6)])

    data = {
        'horoscope': horoscope,
        'animal': animal,
        'icon': icons[icon],
        'color': color
    }

    uid = base64.b64encode('%s|%s|%s|%s' % (horoscope, animal, icon, color))
    data['uid'] = uid

    return data


if __name__ == '__main__':
    app.debug = True
    app.run(port=4000)

