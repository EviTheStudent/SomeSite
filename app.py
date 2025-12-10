from flask import *

# Configure application
app = Flask(__name__)


@app.route("/")
def hello():
    return "Basic Flask App"

@app.route("/about")
def about():
    return "./Imgs/30.png"

if __name__ == '__main__':
    app.run()