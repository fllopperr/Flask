from flask import Flask
from models import Mangaka, Anime, db
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///anime.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        mangakas = [
            Mangaka(name='Eiichiro Oda'),
            Mangaka(name='Masashi Kishimoto'),
            Mangaka(name='Hajime Isayama'),
            Mangaka(name='Gege Akutami'),
            Mangaka(name='Yoshihiro Togashi'),
            Mangaka(name='Tite Kubo')
        ]
        db.session.add_all(mangakas)
        db.session.commit()

        anime_list = [
            Anime(title='One Piece', year='1999', episodes=1124, status='Ongoing', mangaka_id=mangakas[0].id),
            Anime(title='Naruto', year='2002', episodes=220, status='Finished', mangaka_id=mangakas[1].id),
            Anime(title='Naruto Shippuden', year='2007', episodes=500, status='Finished', mangaka_id=mangakas[1].id),
            Anime(title='Attack on Titan', year='2013', episodes=89, status='Finished', mangaka_id=mangakas[2].id),
            Anime(title='Jujutsu Kaisen', year='2020', episodes=47, status='Ongoing', mangaka_id=mangakas[3].id),
            Anime(title='Hunter x Hunter', year='2011', episodes=148, status='Finished', mangaka_id=mangakas[4].id),
            Anime(title='Yu Yu Hakusho', year='1992', episodes=112, status='Finished', mangaka_id=mangakas[4].id),
            Anime(title='Bleach', year='2004', episodes=366, status='Ongoing', mangaka_id=mangakas[5].id)
        ]

        db.session.add_all(anime_list)
        db.session.commit()