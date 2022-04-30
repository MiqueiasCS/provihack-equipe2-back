from flask import Blueprint

from app.controllers.company.signin_company_controller import register_company
from app.controllers.company.update_company_controller import update_company
from app.controllers.company.delete_company_controller import delete_company
from app.controllers.company.get_company_controller import get_all_company,get_one


bp_company = Blueprint('bp_company', __name__,url_prefix='/company')

bp_company.post('/register')(register_company)
bp_company.put('')(update_company)
bp_company.delete('')(delete_company)

bp_company.get('')(get_all_company)
bp_company.get('/<id>')(get_one)
