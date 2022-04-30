from flask import Blueprint

from app.controllers.residues.get_residues import (
    retrieve_one_residue,
    retrieve_residues,
)
from app.controllers.residues.register_controller import register_residue
from app.controllers.residues.update_controller import collect_residue

bp_residues = Blueprint('bp_residues', __name__, url_prefix='/residues')

bp_residues.patch('/<uuid>')(collect_residue)
bp_residues.get('')(retrieve_residues)
bp_residues.get('/<uuid>')(retrieve_one_residue)
bp_residues.post('/register')(register_residue)
