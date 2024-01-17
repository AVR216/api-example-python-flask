from repositories.main_repository import MainRepository

main_repo = MainRepository()

# services/hello_service.py
class MainService:
    
    def get_hello_message(self):
        return "Hello, World!"
    
    def insert_hello_message(self, message):
        return main_repo.insert_hello_message(message)