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


class Matriculas(db.Model):

    __tablename__ = 'matricula'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(200))
    placa = db.Column(db.String(200))
    anoMatricula = db.Column(db.Intenger, nullable=False)
    costo= db.Column(db.Intenger, nullable=False)
     # este atributo no puede ser nulo


    def __repr__(self):
        return "Matriculas: nombre=%s placa=%s anoMatricula=%d costo=%d" % (
                          self.nombre,
                          self.placa,
                          self.anoMatricula,
                          self.costo)

# vista

@app.route('/')
def index():
    matricula = Matriculas.query.all()
    return render_template('index.html', matricula=matricula)


@app.route('/<int:matricula_id>/')
def docente(matricula_id):
    matricula = Matriculas.query.get_or_404(matricula_id)
    return render_template('matricula.html', matricula=matricula)


@app.route('/add/matricula/', methods=('GET', 'POST'))
def crear():
    if request.method == 'POST':
        nombre = request.form['nombre']
        placa = request.form['placa']
        anoMatricula = request.form['anoMatricula']
        costo = request.form['costo']
        matriculacion = Matriculas(nombre=nombre,
                             placa = placa,
                             anoMatricula = anoMatricula,
                             costo = costo
                          )
        db.session.add(matriculacion)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('crear.html')


@app.route('/editar/matricula/<int:matricula_id>/', methods=('GET', 'POST'))
def editar(matricula_id):
    matricula = Matriculas.query.get_or_404(matricula_id)

    if request.method == 'POST':
        nombre = request.form['nombre']
        placa = request.form['placa']
        anoMatricula = request.form['anoMatricula']
        costo= request.form['costo']

        matricula.nombre = nombre
        matricula.placa = placa
        matricula.anoMatricula= anoMatricula
        costo.costo= costo
        db.session.add(matricula)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('editar.html', docente=matricula)
