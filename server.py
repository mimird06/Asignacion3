from flask import Flask, render_template, request
import sqlite3

db = sqlite3.connect('recipy.db', check_same_thread=False)
cursorDB = db.cursor()

servidor = Flask(__name__)

@servidor.route('/')
def inicio():
    return render_template('index.html')

@servidor.route('/agregar')
def agregar():
    return render_template('agregar.html')

@servidor.route('/agregar/datos', methods=['POST'])
def datos():
    
    nombre = request.form['nombre']
    ingredientes = request.form['ingredientes']
    url = request.form['link-img']

    contenedor = (nombre, ingredientes, url)
    cursorDB.execute("INSERT INTO recetas (nombre, ingredientes, link) VALUES (?, ?, ?)", contenedor)
    db.commit()

    alerta = 'Datos se han guardado correctamente.'

    return render_template('agregar.html', alerta=alerta)

@servidor.route('/recetas')
def recetas():

    datos = db.execute('SELECT * FROM recetas')

    return render_template('recetas.html', acept=datos)

if __name__=='__main__':
    servidor.run(debug=True, port=6542)
