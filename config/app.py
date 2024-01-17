# api/app.py
from flask import Flask
from flask_restful import Api
from models.main_model import db
from resourceslocal.main_resource import MainResource #.main_resource import MainResource

app = Flask(__name__)
api = Api(app)

# Configuración de la base de datos MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/test01'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialización de la base de datos
db.init_app(app)

api.add_resource(MainResource, '/hello')

if __name__ == '__main__':
    with app.app_context():
        # Crear las tablas en la base de datos
        db.create_all()
    app.run(debug=True)
