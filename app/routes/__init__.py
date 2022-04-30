from flask import Flask

from app.routes.company_routes import bp_company
from app.routes.residues_routes import bp_residues
from app.routes.user_routes import bp_user


def init_app(app: Flask):
    app.register_blueprint(bp_user)
    app.register_blueprint(bp_company)
    app.register_blueprint(bp_residues)
