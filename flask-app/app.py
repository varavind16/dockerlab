from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://lh3.googleusercontent.com/yLxCqh5-bVTMg8k11XPKwQPOEQydw0yRMOkhnmdZMkcU0WbpZvO2Vpgu3Y2Tjvb28FRdw3Yczu6iKVCcpqVszk1BA-D8vl8VNMR98_th"
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
