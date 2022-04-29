from flask import Flask

from app.routes.user_routes import bp_user
from app.routes.company_routes import bp_company


def init_app(app: Flask):
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_company)
