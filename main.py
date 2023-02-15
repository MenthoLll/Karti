from flask import Flask
import requests


app: Flask = Flask(__name__)

response: requests.Response = requests.get(
    'https://api.hearthstonejson.com/v1/121569/ruRU/cards.collectible.json'
)

cart = response.json()

@app.route('/')
def index():
    result: str = ""
    for i in cart:
        result += f"<h3>Название Карты: {i['name']} <br> id: {i['id']}</h3>"
    return result


if __name__ == '__main__':
    app.run(
        port=8080,
        debug=False
    )