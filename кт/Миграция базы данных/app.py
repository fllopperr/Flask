from flask import redirect, url_for
from flask import Flask, render_template
from models import Student, db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def home():
    return redirect(url_for('students_list'))

@app.route('/students')
def students_list():
    students = Student.query.order_by(Student.surname, Student.name).all()
    return render_template('students.html', students=students)

if __name__ == '__main__':
    app.run(debug=True)