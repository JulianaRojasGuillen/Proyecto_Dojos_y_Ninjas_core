from os import name
from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.model_ninja import Ninja

class Dojo:
    def __init__(self, id, name, created_at, updated_at):
        self.name = name
        self.id = id
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def agregaDojo(cls, nuevoDojo):
        query = "INSERT INTO dojos(name) VALUES (%(name)s);"
        resultado = connectToMySQL("dojos_y_ninjas").query_db(query,nuevoDojo)
        return resultado
    
    @classmethod
    def obtenerListaDojos(cls):
        query = "SELECT * FROM dojos;"
        resultado = connectToMySQL("dojos_y_ninjas").query_db(query)
        listaDojos=[]
        for dojo in resultado:
            listaDojos.append(Dojo(dojo["id"],dojo["name"],dojo["created_at"],dojo["updated_at"]))
        return listaDojos
    
    @classmethod
    def obtieneIDDojo(cls, nameDojo):
        query= "SELECT id FROM dojos WHERE %(name)s = name;"
        resultado = connectToMySQL("dojos_y_ninjas").query_db(query,nameDojo)
        return resultado[0]["id"]
    
    @classmethod
    def obtenerListadeNinjas(cls, dojo):
        query="SELECT first_name, last_name, age FROM ninjas WHERE %(id)s = dojo_id"
        resultado = connectToMySQL("dojos_y_ninjas").query_db(query,dojo)
        listaNinjas=[]
        for ninja in resultado:
            listaNinjas.append(ninja)
        return resultado
