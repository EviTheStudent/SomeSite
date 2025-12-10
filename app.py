from flask import *
import random
# Configure application
app = Flask(__name__)


@app.route("/")
def SRandImg():
    typeOfFile = random.randint(1, 3)
    if typeOfFile == 1:
        imageNumber = random.randint(1, 37)
        return send_file(f"Imgs/{imageNumber}.png", mimetype='image/jpg')
    elif typeOfFile == 2:
        gifNumber = random.randint(1, 8)
        return send_file(f"Gifs/{gifNumber}.gif", mimetype='image/gif')
    else:
        videoNumber = random.randint(1, 5)
        return send_file(f"Videos/{videoNumber}.mp4", mimetype='video/mp4')

@app.route("/about")
def about():
    return send_file("Imgs/30.png", mimetype='image/jpg')

if __name__ == '__main__':
    app.run()
