from app import app
from models import Student, db

def create_students():
    with app.app_context():
        students = [
            Student(
                name="Данил",
                surname="Горбунов",
                age=18,
                course=1,
                direction= "WEB development",
                specialization= "Frontend",
            ),
            Student(
                name="Артём",
                surname="Вилисов",
                age=18,
                course=1,
                direction= "WEB development",
                specialization= "Frontend",
            ),
            Student(
                name="Михаил",
                surname="Скобелкин",
                age=18,
                course=1,
                direction= "WEB development",
                specialization= "Frontend",
            ),
            Student(
                name="Игорь",
                surname="Зеленский",
                age=20,
                course=1,
                direction= "WEB development",
                specialization= "Frontend",
            ),
            Student(
                name="Данил",
                surname="Худой",
                age=18,
                course=1,
                direction= "WEB development",
                specialization= "Frontend",
            ),
            Student(
                name="Иван",
                surname="Сильченко",
                age=18,
                course=1,
                direction= "WEB development",
                specialization= "Frontend",
            ),
        ]
        
        db.session.add_all(students)
        db.session.commit()

if __name__ == '__main__':
    create_students()