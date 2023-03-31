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

if __name__=='__main__':
    servidor.run(debug=True, port=6542)
