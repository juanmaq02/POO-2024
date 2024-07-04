from flask import Flask, request, render_template, redirect, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.py')

from models import db
from models import Paquete, Transporte, Sucursal, Repartidor
from datetime import datetime

@app.route('/')
def inicio():
    return render_template("/inicio.html")

@app.route('/repartidor')
def repartidor():
    return f'No disponible'

@app.route('/despachante', methods = ['GET', 'POST'])
def sucursales():
    if request.method == 'POST':
        return redirect(url_for('despachante', idsucursal = request.form['sucursal']))
    
    return render_template("/sucursales.html", sucursales = Sucursal.query.order_by(Sucursal.numero).all(), hora = datetime.now().hour)

@app.route('/despachante<int:idsucursal>/sucursal')
def despachante(idsucursal):
    session['sucursal_id'] = idsucursal
    datos = Sucursal.query.get(idsucursal)
    return render_template('/despachante.html', sucursal = datos, hora = datetime.now().hour)
    
@app.route('/despachante<int:idsucursal>/registrar_paquete')
def registrar_paquete(idsucursal):
    sucursal = Sucursal.query.get(idsucursal)
    return render_template('/registrar_paquete.html', sucursal = sucursal, idsucursal = idsucursal)

@app.route('/despachante<int:idsucursal>/registrado', methods = ['GET', 'POST'])
def registrado(idsucursal):
    if request.method == 'POST':
        try:
            peso = request.form['peso']
            nombreDestinatario = request.form['nombre']
            direccionDestinatario = request.form['direccion']
            sucursal = Sucursal.query.get(idsucursal)
            if peso == '' or nombreDestinatario == '' or direccionDestinatario == '':
                Epeso = Enombre = Edireccion = False
                if peso == '':
                    Epeso = True
                if nombreDestinatario == '':
                    Enombre = True
                if direccionDestinatario == '':
                    Edireccion = True
                return render_template('/registrar_paquete.html', sucursal = sucursal, Epeso = Epeso, Enombre = Enombre, Edireccion = Edireccion, idsucursal = idsucursal)
            numeroEnvio = 1000 + Paquete.query.count() * 20
            paquete = Paquete(numeroenvio = numeroEnvio, peso = peso, nomdestinatario = nombreDestinatario, dirdestinatario = direccionDestinatario, entregado = False, observaciones = '', idsucursal = 0, idtransporte = 0, idrepartidor = 0)
            db.session.add(paquete)
            db.session.commit()
        except Exception:
            return render_template('/error.html', error = "Se ha producido un error al registrar el paquete.", sucursal = sucursal, idsucursal = idsucursal)
        
        return render_template('/registrado.html', sucursal = sucursal, numeroEnvio = numeroEnvio, idsucursal = idsucursal, numerotransporte = None, fechahorallegada = None)
    
    return redirect(url_for('registrar_paquete', sucursal = sucursal, idsucursal = idsucursal))

@app.route('/despachante<int:idsucursal>/salida_transporte', methods = ['GET', 'POST'])
def salida_transporte(idsucursal):
    sucursal = Sucursal.query.get(idsucursal)
    if request.method == 'POST':
        idpaquetes = []
        idpaquetes = request.form.getlist('paquete_id')
        try:
            idtransporte = Transporte.query.count() + 1
            numerotransporte = Transporte.query.count() + 214
            fechahorasalida = datetime.now()
            idsucursal = request.form['sucursal']
            print(idsucursal)
            transporte = Transporte(id = idtransporte, numerotransporte = numerotransporte, fechahorasalida = fechahorasalida, fechahorallegada = '', idsucursal = idsucursal)
            db.session.add(transporte)
            bandera = True
            for idpaquete in idpaquetes:
                bandera = False
                paquete = Paquete.query.get(idpaquete)
                paquete.idtransporte = idtransporte
                paquete.idsucursal = idsucursal
                db.session.commit()
            if bandera:
                raise Exception
        except Exception:
            return render_template('/error.html', error = "Se ha producido un error al asignar un transporte.", sucursal = sucursal, idsucursal = idsucursal)

        return render_template('/registrado.html', sucursal = sucursal, numeroEnvio = None, idsucursal = idsucursal, numerotransporte = numerotransporte, fechahorallegada = None)

    return render_template('/salida_transporte.html', sucursales = Sucursal.query.order_by(Sucursal.numero).all(), sucursal = sucursal, idsucursal = idsucursal, paquetes = Paquete.query.order_by(Paquete.id).all())

@app.route('/despachante<int:idsucursal>/llegada_transporte', methods = ['GET', 'POST'])
def llegada_transporte(idsucursal):
    sucursal = Sucursal.query.get(idsucursal)
    if request.method == 'POST':
        try:
            transporte = Transporte.query.get(request.form['transporte_id'])
            transporte.fechahorallegada = datetime.now()
            db.session.commit()
        except Exception:
            return render_template('/error.html', error = "Se ha producido un error al registrar la llegada de un transporte.", sucursal = sucursal, idsucursal = idsucursal)
        
        return render_template('/registrado.html', sucursal = sucursal, numeroEnvio = None, idsucursal = idsucursal, numerotransporte = None, fechahorallegada = transporte.fechahorallegada)
    
    return render_template('/llegada_transporte.html', sucursal = sucursal, idsucursal = idsucursal, transportes = Transporte.query.order_by(Transporte.id).all())

@app.route('/despachante<int:idsucursal>/asignar_repartidor')
def asignar_repartidor(idsucursal):
    return f'No disponible'

if __name__ == '__main__':
    app.run(debug=True)