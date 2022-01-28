from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.model_dojo import Dojo


@app.route( '/', methods=['GET'] )
def despliegaDojos():
    return render_template ("newDojo.html",dojos=Dojo.obtenerListaDojos())

@app.route('/newDojo', methods=['POST'])
def registraDojo():
    nuevoDojo={
        "name": request.form["newDojoName"]
    }
    resultado = Dojo.agregaDojo(nuevoDojo)
    return redirect('/')



