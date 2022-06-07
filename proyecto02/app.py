"""
    Tomado de https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
"""

import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy.sql import func
basedir = os.path.abspath(os.path.dirname(__file__))
from config import enlace
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = enlace 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Docente(db.Model):

    __tablename__ = 'docentes'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    placa = db.Column(db.String(200), nullable=False)
    anio = db.Column(db.String(200), nullable=False) # este atributo no puede ser nulo
    costo = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return "Matricula: nombre=%s placa=%s año:%s % costo=%s "(
                          self.nombre,
                          self.placa,
                          self.anio,
                          self.costo)

# vista

@app.route('/')
def index():
    docentes = Docente.query.all()
    return render_template('index.html', docentes=docentes)


@app.route('/<int:docente_id>/')
def docente(docente_id):
    docente = Docente.query.get_or_404(docente_id)
    return render_template('docente.html', docente=docente)


@app.route('/add/docente/', methods=('GET', 'POST'))
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        placa = request.form['placa']
        anio = request.form['anio']
        costo = request.form['costo']
        profesor = Docente(nombre=nombre,
                          placa=placa,
                          anio=anio,
                          costo=costo,
                          )
        db.session.add(profesor)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('crear.html')


@app.route('/editar/docente/<int:docente_id>/', methods=('GET', 'POST'))
def editar(docente_id):
    docente = Docente.query.get_or_404(docente_id)

    if request.method == 'POST':
        nombre = request.form['nombre']
        placa = request.form['placa']
        anio = request.form['anio']
        costo = request.form['costo']

        docente.nombre = nombre
        docente.placa = placa
        docente.anio = anio
        docente.costo = costo
        db.session.add(docente)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('editar.html', docente=docente)
