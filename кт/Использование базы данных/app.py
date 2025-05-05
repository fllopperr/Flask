from flask import Flask, render_template
from models import Mangaka, Anime, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anime.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)


@app.route('/anime')
def anime_list():
    anime_list = Anime.query.all()
    return render_template('anime.html', anime_list=anime_list)

if __name__ == '__main__':
    app.run(debug=True)