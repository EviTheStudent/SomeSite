from flask import *

# Configure application
app = Flask(__name__)


@app.route("/")
def hello():
    return "Basic Flask App"

@app.route("/about")
def about():
 return send_file("Imgs/30.png", mimetype='image/jpg')

if __name__ == '__main__':
    app.run()
