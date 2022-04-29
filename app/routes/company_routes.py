from flask import Blueprint

from app.controllers.company.signin_company_controller import register_company
from app.controllers.company.update_company_controller import update_user

bp_company = Blueprint('bp_company', __name__,url_prefix='/company')

bp_company.post('/register')(register_company)
bp_company.put('')(update_user)