from flask import Blueprint

from app.controllers.company.signin_company_controller import register_company
from app.controllers.company.update_company_controller import update_company
from app.controllers.company.delete_company_controller import delete_company

from app.controllers.residues.update_controller import collect_residue

bp_company = Blueprint('bp_company', __name__,url_prefix='/company')

bp_company.post('/register')(register_company)
bp_company.put('')(update_company)
bp_company.delete('')(delete_company)
bp_company.patch('/residue/<uuid>')(collect_residue)