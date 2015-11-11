import io
import json
import os
import re

from flask import Flask
from flask_restful import inputs, reqparse
from PIL import Image
from signals.settings import ASSETS_DIR
from werkzeug.exceptions import BadRequest

app = Flask('signals')


RE_NOT_LETTER = re.compile(r'[^A-Za-z0-9!@#$]+')


def json_response(data, code=200, headers=None):
    if headers is None:
        headers = {}
    headers.setdefault('Content-type', 'application/json')
    return json.dumps(data), code, headers


@app.errorhandler(400)
def handle_bad_request(error):
    if hasattr(error, 'data'):
        return json_response(error.data, 400)
    return json_response({'message': error.description}, 400)


def get_flag_images():
    flags = []
    flags.extend((x, x) for x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
    flags.extend([('!', 'R1'), ('@', 'R2'), ('#', 'R3'), ('$', 'R4')])

    for tl, fl in flags:
        filename = os.path.join(ASSETS_DIR, 'flags', '{}.png'.format(fl))
        img = Image.open(filename)
        # img = img.resize((FLAG_WIDTH, FLAG_HEIGHT))
        yield tl, img

# FLAG_WIDTH = FLAG_HEIGHT = 100
FLAGS_IMAGES = dict(get_flag_images())  # pre-cache


def parse_color(s):
    if len(s) == 6:
        return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))
    if len(s) == 3:
        return (int(s[0] * 2, 16), int(s[1] * 2, 16), int(s[2] * 2, 16))
    raise ValueError('Color must be three or six hexadecimal digits')




@app.route('/flags/<text>')
def nautical_flags(text):
    TEXT_SIZE_LIMIT = 100  # just to prevent abuse

    parser = reqparse.RequestParser()
    parser.add_argument('row_size', type=inputs.positive, default=10)
    parser.add_argument('size', type=inputs.int_range(10, 100), default=100)
    parser.add_argument('padding', type=inputs.int_range(0, 50), default=10)
    parser.add_argument('background', type=parse_color,
                        default=(0xC8, 0xD0, 0xD4))

    args = parser.parse_args()

    ROW_SIZE = args['row_size']
    FLAG_WIDTH = FLAG_HEIGHT = args['size']
    PADDING = args['padding']
    BACKGROUND = args['background']

    if len(text) > TEXT_SIZE_LIMIT:
        raise BadRequest('Text too long')

    text = text.upper()
    text = RE_NOT_LETTER.sub(' ', text)
    text = text.strip()

    def _tokenize(t):
        while t:
            yield t[:ROW_SIZE]
            t = t[ROW_SIZE:]

    rows = list(_tokenize(text))
    if len(rows) == 0:
        raise BadRequest('Text must contain at least one flag')

    img_width = (PADDING + FLAG_WIDTH) * len(rows[0]) + PADDING
    img_height = (PADDING + FLAG_HEIGHT) * len(rows) + PADDING

    img = Image.new('RGBA', (img_width, img_height), color=BACKGROUND)
    hoff = voff = PADDING

    for row in rows:
        for letter in row:
            letter_img = FLAGS_IMAGES.get(letter)

            if letter_img:
                scaled = letter_img.resize((FLAG_WIDTH, FLAG_HEIGHT))
                img.paste(scaled, box=(hoff, voff), mask=scaled)

            hoff += FLAG_WIDTH + PADDING
        hoff = PADDING
        voff += FLAG_HEIGHT + PADDING

    output = io.BytesIO()
    img.save(output, 'png')

    return output.getvalue(), 200, {'content-type': 'image/png'}
