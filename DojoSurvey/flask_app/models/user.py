from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class User:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.dojo_locsation = data['dojo_locsation']
        self.favorite_lenguage= data['favorite_lenguage']
        self.coments = data['coments']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM user;"
        results = connectToMySQL('user_dojo').query_db(query)
        # guarda el resultado de la bd

        users = []
        # crea arreglo para guiardar los valores 
        for user in results: #itera los nombres de la base de datos 
            users.append(cls(user))
            # flos mete en el arreglo -y los convierte en una clkase ususario
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO user ( name , dojo_locsation , favorite_lenguage , coments ) VALUES ( %(name)s , %(dojo_locsation)s , %(favorite_lenguage)s , %(coments)s );"
        # los nombres deben ser los de la bd / los valores los del html
        return connectToMySQL('user_dojo').query_db(query, data)

    @classmethod
    def get_user_by_id(cls, new_data):
        query = "SELECT * FROM user WHERE id = %(id)s"
        results = connectToMySQL('user_dojo').query_db(query, new_data)
        return cls(results[0])

    @staticmethod
    def validate_user(user):
        # print("Validating Form")
        # print(len(user['dojo_locsation']))
        # print( user['favorite_lenguage'])
        # print( user['favorite_lenguage'] == 0)
        is_valid = True # we assume this is true
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['dojo_locsation']) == 0:
            flash("Must choose a Dojo Location.")
            is_valid = False
        if len(user['favorite_lenguage']) == 0:
            flash("Must choose a favorite lenguage.")
            is_valid = False
        if len(user['comments']) < 3:
            flash("coments must be at least 3 characters.")
            is_valid = False
        return is_valid
