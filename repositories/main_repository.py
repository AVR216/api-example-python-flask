# repositories/hello_repository.py
from models.main_model import Hello, db

class MainRepository:
    def insert_hello_message(self, message):
        new_hello = Hello(message=message)
        db.session.add(new_hello)
        db.session.commit()
        return new_hello
