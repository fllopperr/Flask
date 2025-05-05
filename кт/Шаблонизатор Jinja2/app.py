from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def show_resume():
    resume_data = {
        'name': 'Данил Горбунов',
        'job': 'Программист архитектор',
        'about': 'Хочу найти работу в IT',
        'skills': ['Хорош во всём'],
    }
    return render_template('resume.html', resume=resume_data)

if __name__ == '__main__':
    app.run(debug=True)