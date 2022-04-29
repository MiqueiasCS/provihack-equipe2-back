from app.models.user_model import UserModel, UserSchema
from http import HTTPStatus


def retrieve_users():
    user_schema = UserSchema()
    users  = UserModel.query.all()

    return user_schema.dumps(users, many=True), HTTPStatus.OK