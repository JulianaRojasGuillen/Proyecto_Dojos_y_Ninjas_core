from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.model_dojo import Dojo
from flask_app.models.model_ninja import Ninja

@app.route('/newNinja', methods=['GET'])
def despliegaFormularioNinja():
    return render_template("newNinja.html", dojos=Dojo.obtenerListaDojos())

@app.route('/newNinja', methods=['POST'])
def registraNinja():
    nameDojo={}
    nameDojo["name"]= request.form["selectedDojo"]

    nuevoNinja={
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "age": request.form["age"],
        "dojo_id": Dojo.obtieneIDDojo(nameDojo)
    }
    resultado = Ninja.agregaNinja(nuevoNinja)
    return redirect ('/newNinja')

@app.route('/listaNinjas/<dojo_id>', methods=['GET'])
def despliegaNinjas(dojo_id):
    dojo={
        "id": dojo_id
    }
    listaNinjas = Dojo.obtenerListadeNinjas(dojo)
    return render_template("listaNinjas.html", ninjas=listaNinjas)