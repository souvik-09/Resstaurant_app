from flask import Flask, jsonify,request
from flask_sqlalchemy import SQLAlchemy
from models.customer import Customer 
from models.orders import Orders
from models.restaurant import Restaurant
from config import db, SECRET_KEY
from flask_migrate import Migrate

app = Flask(__name__)
db.init_app(app)
migrate = Migrate(app, db)



app.config['SECRET_KEY'] = "weaksecretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:Souvikpgadmin@localhost/restaurant_app"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



@app.post("/signup")
def signup():
    form = request.form.to_dict(flat=True)
    existing_user = Customer.query.filter_by(phone=form['phone']).first()

    if existing_user is None:
        new_user = Customer(
            name=form['name'],
            phone=form['phone'],
        )

        new_user.set_password(password=form['password'])

        db.session.add(new_user)
        db.session.commit()

        return jsonify(msg= "Signup successful")
    else:
        return jsonify(msg="User already exist")

@app.post("/login")
def login():
    form = request.form.to_dict(flat=True)
    user = Customer.query.filter_by(phone=form['phone']).first()

    if user:
        if user.check_password(form['password']):
            return jsonify(msg="Login successful")      
    else:
        return jsonify(msg="Incorrect phone number or password")


@app.post("/signup_seller")
def signup_seller():
    form = request.form.to_dict(flat=True)
    existing_user = Customer.query.filter_by(phone=form['phone']).first()

    if existing_user is None:
        new_user = Customer(
            name=form['name'],
            phone=form['phone'],
        )

        new_user.set_password(password=form['password'])

        db.session.add(new_user)
        db.session.commit()

        return jsonify(msg="Selller signup  successful")
    else:
        return jsonify(msg="Seller already exist")

@app.post("/login_seller")
def seller_login():
    form = request.form.to_dict(flat=True)
    user = Customer.query.filter_by(phone=form['phone']).first()

    if user:
        if user.check_password(form['password']):
            return jsonify(msg="Login successful")      
    else:
        return jsonify(msg="Incorrect phone number or password")



@app.post('/add_menu_items')
def add_item():
    if request.method == 'POST':
        menu_items = request.form['menu_items']
        item_price = request.form['item_price']
        
        item = Restaurant(menu_items=menu_items, item_price=item_price)
        db.session.add(item)
        db.session.commit()
        
        return jsonify(msg='Item added')
    else:
        return jsonify(msg='This endpoint only accepts POST requests')
 
 
@app.get('/')
def all_menu():
    menu_items = Restaurant.query.all()
    items = [{"id": restaurant.id,"name": restaurant.menu_items, "price": restaurant.item_price,
              "item_rating": restaurant.item_rating} for restaurant in menu_items]
    return jsonify(items)


@app.post('/order')
def order():
    if request.method == 'POST':

        menu_item_id = request.form.get('menu_item_id')
        quantity = request.form.get('quantity')
      
        menu_item = Restaurant.query.get(menu_item_id)
        total_amount = menu_item.item_price * int(quantity)
        
        order = Orders(quantity=quantity, total_amount=total_amount)
        db.session.add(order)
        db.session.commit()
        return jsonify(msg='Order Confirmed', order_id=order.id, total_amount=total_amount)
    else:
        return jsonify(msg='This endpoint only accepts POST requests')
    

@app.post('/rate')
def rate():
    if request.method == 'POST':
        
        menu_item_id = request.form.get('menu_item_id')
        item_rating = request.form.get('item_rating')
            
        if not menu_item_id:
            return jsonify(error='menu_item_id is required'), 400
        if not item_rating:
            return jsonify(error='item_rating is required'), 400
        if not item_rating.isdigit() or int(item_rating) not in range(1, 6):
            return jsonify(error='item_rating must be a number between 1 and 5'), 400

        
        menu_item = Restaurant.query.get(menu_item_id)
        if not menu_item:
            return jsonify(error='menu item not found'), 404

        
        menu_item.item_rating = item_rating
        db.session.add(menu_item)
        db.session.commit()
        return jsonify(msg='Thank you for your feedback!')
    else:
        return jsonify(error='This endpoint only accepts POST requests'), 405



        

# from app import app, db
# with app.app_context():
#         db.create_all()
        
if __name__ == '__main__':
    app.run(debug=True)