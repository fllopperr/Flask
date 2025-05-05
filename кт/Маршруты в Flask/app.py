from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def greeting():
    current_time = datetime.now().hour
    if 6 <= current_time < 12:
        greeting_msg = "Доброе утро"
    elif 12 <= current_time < 18:
        greeting_msg = "Добрый день"
    elif 18 <= current_time < 24:
        greeting_msg = "Добрый вечер"
    else:
        greeting_msg = "Доброй ночи"
    
    return render_template('index.html', greeting=greeting_msg)

if __name__ == '__main__':
    app.run(debug=True)