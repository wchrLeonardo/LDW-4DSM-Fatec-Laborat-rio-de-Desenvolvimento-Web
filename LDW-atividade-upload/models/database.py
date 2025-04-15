from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    folders = db.relationship('Folder', backref='user', lazy=True)

    def __init__(self, name, user, password):
        self.name = name
        self.user = user
        self.password = password

    def __repr__(self):
        return f"<User {self.name}>"

class Folder(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable=False)
    data_date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    photos = db.relationship('Photo', backred='folder', lazy=True)

    def __init__(self, name, data_date, user_id):
        self.name = name
        self.data_date = data_date
        self.user_id = user_id
    
    def __repr__(self):
        return f"<Folder {self.name}>"

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    filename = db.Column(db.String(255), nullable=False)  
    folder_id = db.Column(db.Integer, db.ForeignKey('folder.id'), nullable=False)  

    def __init__(self, filename, folder_id):
        self.filename = filename
        self.folder_id = folder_id
        
    def __repr__(self):
        return f"<Photo {self.filename}>"
        