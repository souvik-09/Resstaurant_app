
# def token_required(f):
#     @wraps(f)
#     def decorator(*args, **kwargs):
#         token = None

#         if 'x-access-tokens' in request.headers:
#             token = request.headers['x-access-tokens']

#         if not token:
#             return jsonify(message="valid token is missing")

#         try:
#             data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#             current_user = Customer.query.filter_by(registration_token=data['public_id']).first()
#         except:
#             return jsonify(message="token is invalid")
#         return f(current_user, *args, **kwargs)
#     return decorator

# def access_required(role="ANY"):
#     def wrapper(fn):
#         @wraps(fn)
#         def decorated_view(*args, **kwargs):
#             if session.get("role") == None or role == "User":
#                 session["header"] = "Welcome User!!"
#                 print("Guest session started")
#             if session.get("role") == "seller" and role == "seller":
#                 session["header"] = "Welcome Seller!!"
#                 print("access: seller")
#             else:
#                 session["header"] = "Sorry No Access"
#                 print("No access")
#             return fn(*args, **kwargs)
#         return decorated_view
#     return wrapper