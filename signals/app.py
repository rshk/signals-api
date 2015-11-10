import os
import io

from flask import Flask, request
from PIL import Image
import re

from signals.settings import ASSETS_DIR

app = Flask('signals')


RE_NOT_LETTER = re.compile(r'[^A-Z]+')


def get_flag_images():
    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        filename = os.path.join(ASSETS_DIR, 'flags', '{}.png'.format(letter))
        img = Image.open(filename)
        img = img.resize((FLAG_WIDTH, FLAG_HEIGHT))
        yield letter, img

FLAG_WIDTH = FLAG_HEIGHT = 100
FLAGS_IMAGES = dict(get_flag_images())  # pre-cache


def parse_color(s):
    if len(s) == 6:
        return (int(s[0:2], 16), int(s[2:4], 16), int(s[4:6], 16))
    if len(s) == 3:
        return (int(s[0] * 2, 16), int(s[1] * 2, 16), int(s[2] * 2, 16))
    raise ValueError('Invalid length')


@app.route('/flags/<text>')
def nautical_flags(text):
    ROW_SIZE = 8
    PADDING = 10  # pixel
    BACKGROUND = (0x88, 0x88, 0x88)

    if 'row_size' in request.args:
        try:
            ROW_SIZE = max(int(request.args['row_size']), 1)
        except ValueError:
            return 'Bad parameter: row_size', 400

    if 'background' in request.args:
        try:
            BACKGROUND = parse_color(request.args['background'])
        except ValueError:
            return 'Bad parameter: background', 400

    text = text.upper()
    text = RE_NOT_LETTER.sub(' ', text)
    text = text.strip()

    def _groups(t):
        while t:
            yield t[:ROW_SIZE]
            t = t[ROW_SIZE:]

    rows = list(_groups(text))
    if len(rows) == 0:
        return 'Empty text', 400

    img_width = (PADDING + FLAG_WIDTH) * len(rows[0]) + PADDING
    img_height = (PADDING + FLAG_HEIGHT) * len(rows) + PADDING

    img = Image.new('RGB', (img_width, img_height), color=BACKGROUND)
    hoff = voff = PADDING

    for row in rows:
        for letter in row:
            letter_img = FLAGS_IMAGES.get(letter)
            if letter_img:
                img.paste(letter_img, (hoff, voff))
            hoff += FLAG_WIDTH + PADDING
        hoff = PADDING
        voff += FLAG_HEIGHT + PADDING

    output = io.BytesIO()
    img.save(output, 'png')

    return output.getvalue(), 200, {'content-type': 'image/png'}
