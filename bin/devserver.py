import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from signals import app

app.run(debug=True)
