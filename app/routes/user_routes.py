from flask import Blueprint
from flask_jwt_extended import jwt_required

from app.controllers.user.delete_controller import delete_user
from app.controllers.user.login_controller import login_user
from app.controllers.user.retrieve_controllers import retrieve_users
from app.controllers.user.signin_controller import register_user
from app.controllers.user.update_address_controller import update_address
from app.controllers.user.update_controller import update_user
from app.controllers.residues.register_controller import register_residue

bp_user = Blueprint('bp_user', __name__)

bp_user.post('/user/register')(register_user)
bp_user.post('/login')(login_user)
bp_user.get('/user')(retrieve_users)
bp_user.delete('/user')(delete_user)
bp_user.put('/user')(update_user)
<<<<<<< HEAD
bp_user.post('/user/residue/register')(jwt_required
()(register_residue))
=======
bp_user.put('/user/address')(update_address)
>>>>>>> 5736181cc4b5756d0fe66611278babf6d518af71
