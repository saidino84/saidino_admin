from app import db

class User(db.Model):
    __tablename__="users"
    id =db.Column(db.Integer, primary_key=True)
    username =db.Column(db.String, unique=True)
    password =db.Column(db.String)
    name =db.Column(db.String)
    email = db.Column(db.String, unique=True)

    def __init__(self, username:str, password:str, name:str, email:str)->None:
        self.username=username
        self.email=email
        self.password=password
        self.name=name
    