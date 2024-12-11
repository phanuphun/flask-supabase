from app.router.books_route import books_route
from app.router.categories_route import categories_route
from app.router.login_route import login_route

def registration_routes(app):
    app.register_blueprint(books_route)
    app.register_blueprint(categories_route)
    app.register_blueprint(login_route)