from flask import *
from math import Random

# Configure application
app = Flask(__name__)


@app.route("/")
def SelectRand():
    str imageNumber = Random(1, 37)
    return send_file(f"Imgs/{imageNumber}.png", mimetype='image/jpg')

@app.route("/about")
def about():
    return send_file("Imgs/30.png", mimetype='image/jpg')

if __name__ == '__main__':
    app.run()