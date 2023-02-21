from flask import Flask, render_template
import os
import random

app = Flask(__name__)

# list of cat images
images = [
    "https://lh3.googleusercontent.com/FAwG0i0L8Md_HeftKg_OUt0l0Ca92ZFSn-UmKTMsbDzrNEwjtb2puIRZMmAuWwdWIYpOIJFIc7S-GnGROl6AW4hG92PPHG73hJmwTk-L"
]


@app.route("/")
def index():
    url = random.choice(images)
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
