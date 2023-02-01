from config import db

class Orders(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer()) 
    total_amount = db.Column(db.DECIMAL(10, 2))
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    customer = db.relationship('Customer', backref='orders') 
    restaurant = db.relationship('Restaurant', backref='orders')   
    
    
    
    