from flask import Flask, redirect, url_for, render_template, request
from datetime import datetime

app = Flask(__name__)


#Context processor
@app.context_processor
def date_now():
    return{
        'now':datetime.utcnow()
    }


#endpoints
@app.route('/')
def index():
    lista = ['Marcelo','Carvajal','Sergio','Raphael']
    return render_template("index.html", lista = lista)

@app.route('/info/<string:nombre>/<apellidos>')
def informacion(nombre, apellidos):
    return f'<h1>Página de información , Hola {nombre} {apellidos}</h1>'    

@app.route('/contact')
@app.route('/contact/<redirecto>')
def contacto(redirecto=None):
    if redirecto is not None :
     return redirect(url_for('lenguajes'))

    return '<h1>Página de contacto</h1>'  

@app.route('/leng')
def lenguajes():
    nombre = "David"
    return render_template("lenguajes.html" , 
        nombre=nombre
    )          

if __name__ == '__main__':
    app.run(debug=True)