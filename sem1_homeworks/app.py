from flask import Flask, render_template

app = Flask(__name__)

bd = {
    "cloth": [
        {"name": "shirt", "img": "image/shirt.jpg", "desc": "This is a shirt", "price": 3100},
        {"name": "shirt", "img": "image/shirt.jpg", "desc": "This is a shirt", "price": 3100},
        {"name": "shirt", "img": "image/shirt.jpg", "desc": "This is a shirt", "price": 3100},
        {"name": "shirt", "img": "image/shirt.jpg", "desc": "This is a shirt", "price": 3100},
        {"name": "shirt", "img": "image/shirt.jpg", "desc": "This is a shirt", "price": 3100},
    ],
    "boots": [
        {"name": "boots", "img": "image/boot.png", "desc": "This is boots", "price": 4100},
        {"name": "boots", "img": "image/boot.png", "desc": "This is boots", "price": 4100},
        {"name": "boots", "img": "image/boot.png", "desc": "This is boots", "price": 4100},
        {"name": "boots", "img": "image/boot.png", "desc": "This is boots", "price": 4100},
    ],
    "jackets": [
        {"name": "jacket", "img": "image/jacket.png", "desc": "This is a jacket", "price": 5100},
        {"name": "jacket", "img": "image/jacket.png", "desc": "This is a jacket", "price": 5100},
        {"name": "jacket", "img": "image/jacket.png", "desc": "This is a jacket", "price": 5100},
        {"name": "jacket", "img": "image/jacket.png", "desc": "This is a jacket", "price": 5100},
        {"name": "jacket", "img": "image/jacket.png", "desc": "This is a jacket", "price": 5100},
        {"name": "jacket", "img": "image/jacket.png", "desc": "This is a jacket", "price": 5100},
    ],
}


@app.route("/")
def index():
    content = {
        "home": "active",
    }
    return render_template("index.html", content=content)


@app.route("/cloth/")
def cloth():
    content = {
        "cloth": "active",
        "items": bd["cloth"]
    }
    return render_template("cloth.html", content=content)


@app.route("/boots/")
def boots():
    content = {
        "boots": "active",
        "items": bd["boots"]
    }
    return render_template("boots.html", content=content)


@app.route("/jacket/")
def jacket():
    content = {
        "jacket": "active",
        "items": bd["jackets"]
    }
    return render_template("jackets.html", content=content)


if __name__ == '__main__':
    app.run(debug=True)
