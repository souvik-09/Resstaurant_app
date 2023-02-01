from config import db
from werkzeug.security import check_password_hash, generate_password_hash

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=True)
    phone = db.Column(db.Integer, nullable=True, unique=True)
    password = db.Column(db.String(500), nullable=True)
    given_rating = db.Column(db.String(500), nullable=True)
    registration_token = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(200), nullable=True)
 
    
    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    def set_registration_token(self, token):
        self.registration_token = token
        
    def check_password(self, password):
        return check_password_hash(self.password, password)                    

    