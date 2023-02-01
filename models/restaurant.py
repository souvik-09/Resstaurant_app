from config import db


class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    menu_items = db.Column(db.String(50))
    item_price = db.Column(db.DECIMAL(10, 2)) # 10 digits with 2 decimal places
    item_rating = db.Column(db.DECIMAL(5,2))