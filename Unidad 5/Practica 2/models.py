from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class Paquete(db.Model):
    __tablename__ = 'paquete'
    id = db.Column(db.Integer, primary_key = True)
    numeroenvio = db.Column(db.Integer, nullable = False)
    peso = db.Column(db.Float, nullable = False)
    nomdestinatario = db.Column(db.String(80), nullable = False)
    dirdestinatario = db.Column(db.String(120), nullable = False)
    entregado = db.Column(db.Boolean, nullable = False)
    observaciones = db.Column(db.Text, nullable = True)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'))
    transporte = db.relationship('Transporte', backref = 'paquete')

class Transporte(db.Model):
    __tablename__ = 'transporte'
    id = db.Column(db.Integer, primary_key = True)
    numerotransporte = db.Column(db.Integer, nullable = False)
    fechahorasalida = db.Column(db.String, nullable = False)
    fechahorallegada = db.Column(db.String, nullable = False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))

class Sucursal(db.Model):
    __tablename__ = 'sucursal'
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer, nullable = False)
    provincia = db.Column(db.String(80), nullable = False)
    localidad = db.Column(db.String(80), nullable = False)
    direccion = db.Column(db.String(120), nullable = False)
    transporte = db.relationship('Transporte', backref = "sucursal")
    paquete = db.relationship('Paquete', backref = "sucursal")
    repartidor = db.relationship('Repartidor', backref = "sucursal")

class Repartidor(db.Model):
    __tablename__ = 'repartidor'
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer, nullable = False)
    nombre = db.Column(db.String(80), nullable = False)
    dni = db.Column(db.Integer, nullable = False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    paquete = db.relationship('Paquete', backref = "repartidor")
