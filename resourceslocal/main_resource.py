# api/resources/hello_resource.py
from flask_restful import Resource, reqparse
from controllers.main_controller import MainController

main_controller = MainController()

class MainResource(Resource):
    def get(self):
        return {'message': main_controller.get_hello_message()}
    
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('message', type=str, required=True, help='Message cannot be blank')
        args = parser.parse_args()

        new_hello = main_controller.insert_hello_message(args['message'])
        return {'id': new_hello.id, 'message': new_hello.message}, 201 
