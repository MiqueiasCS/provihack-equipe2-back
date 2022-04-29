from flask import Blueprint

from app.controllers.user.delete_controller import delete_user
from app.controllers.user.login_controller import login_user
from app.controllers.user.signin_controller import register_user
from app.controllers.user.update_controller import update_user

bp_user = Blueprint('bp_user', __name__)

bp_user.post('/user/register')(register_user)
bp_user.post('/login')(login_user)
bp_user.delete('/user')(delete_user)
bp_user.put('/user')(update_user)
