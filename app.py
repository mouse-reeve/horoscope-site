''' a generative horoscope site '''
from flask import Flask
from horoscope_generator import HoroscopeGenerator
import json
import random

# Config
APP = Flask(__name__)


@APP.route('/api/horoscope', methods=['GET'])
def get_horoscope():
    ''' Get a generated horoscope '''
    sentences = []
    for _ in range(random.randint(3, 7)):
        sentences.append(HoroscopeGenerator.format_sentence(HoroscopeGenerator.get_sentence()))
    return json.dumps({'horoscope': '%s.' % '. '.join(sentences)})


if __name__ == '__main__':
    APP.debug = True
    APP.run(port=4000)

