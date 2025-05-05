from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Денег нет, но вы держитесь"

if __name__ == '__main__':
    app.run(debug=True)