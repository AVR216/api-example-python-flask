# api/controllers/item_controller.py
from flask import request
from services.main_service import MainService

main_service = MainService()

class MainController:
    
    def get_hello_message(self):
        return main_service.get_hello_message()
    
    def insert_hello_message(self, message):
        print(message)
        return main_service.insert_hello_message(message)