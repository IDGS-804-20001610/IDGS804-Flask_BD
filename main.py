from flask import Flask, render_template, request, redirect, url_for, jsonify
from config import DevelopmentConfig
from flask_wtf.csrf import CSRFProtect

from models import db, Alumnos
from decouple import config
import pymysql
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

def get_connection():
    return pymysql.connect(
        host = config('MYSQL_HOST'),
        database = config('MYSQL_DB'),
        user = config('MYSQL_USER'),
        password = config('MYSQL_PASSWORD')

    )

@app.route('/', methods = ['GET', 'POST'])
def index():
    create_form = forms.UserForm(request.form)
    if request.method == 'POST':
        alum = Alumnos(nombre = create_form.nombre.data,
                      apaterno = create_form.apaterno.data,
                      email = create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('index.html', form = create_form)

@app.route("/ABCompleto", methods = ['GET', 'POST'])
def ABCompleto():
    create_form = forms.UserForm(request.form)

    #SELECT * FROM ALUMNOS
    #alumnos = Alumnos.query.all()
    #print(alumnos)
    sql = "CALL get_alumnos();"
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(sql)

    alumnos = cursor.fetchall()
    print(alumnos)
    conn.commit()

    return render_template('ABCompleto.html', form = create_form, alumnos = alumnos)

@app.route("/modificar", methods = ['GET', 'POST'])
def modificar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')

        #SELECT * FROM ALUMNOS WHERE ID = ID
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.email.data = alum1.email

    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = create_form.nombre.data
        alum.apaternos = create_form.apaterno.data
        alum.email = create_form.email.data
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('modificar.html', form = create_form)

@app.route("/eliminar", methods = ['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    if request.method == 'GET':
        id = request.args.get('id')

        #SELECT * FROM ALUMNOS WHERE ID = ID
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.email.data = alum1.email

    if request.method == 'POST':
        id = create_form.id.data
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = create_form.nombre.data
        alum.apaternos = create_form.apaterno.data
        alum.email = create_form.email.data
        db.session.delete(alum)
        db.session.commit()
        return redirect(url_for('ABCompleto'))
    return render_template('eliminar.html', form = create_form)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    app.run(port = 7000)