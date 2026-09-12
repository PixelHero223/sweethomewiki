from flask import Flask, render_template, url_for
from settings import *
from sql_queries import *

app = Flask(__name__)

#головна сторінка
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#старт
@app.route('/start')
def start_page():
    return render_template('start.html')

#правила
@app.route('/rules')
def rules():
    return render_template('rules.html')

#економіка
@app.route('/economy')
def economy():
    return render_template('economy.html')

#команди
@app.route('/commands')
def commands():
    return render_template('commands.html')

#набір в команду
@app.route('/staff')
def staff():
    return render_template('staff.html')

#скіли
@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/skills/<skill_name>')
def skill_page(skill_name):
    return render_template(f'skills/{skill_name}.html')

#статистика
@app.route('/stats')
def stats():
    return render_template('stats.html')

#повідомлення
@app.route('/msg')
def msg():
    return render_template('msg.html')
#статуси
@app.route('/donate')
def donate():
    return render_template('donate.html')

#Адміністрація
@app.route('/aftor')
def aftor():
    return render_template('aftor.html')

if __name__ == '__main__':
    app.run(debug = True)

