from http import HTTPStatus
from flask_jwt_extended import get_jwt_identity, jwt_required
from sqlalchemy.orm import Query

from app.models.user_model import UserModel, UserSchema
from app.models.company_model import CompanyModel, CompanySchema



def retrieve_users():
    user_schema = UserSchema()
    users = UserModel.query.all()

    return user_schema.dumps(users, many=True), HTTPStatus.OK

@jwt_required()
def retrieve_logged_user():
    email = get_jwt_identity()
    user_query: Query = UserModel.query
    company_query: Query = CompanyModel.query

    user_schema = UserSchema()
    company_schema = CompanySchema()

    user: UserModel = user_query.filter_by(email=email).first()
    company: CompanyModel = company_query.filter_by(email=email).first()

    if user:
        return user_schema.dump(user), HTTPStatus.OK
    if company:
        return company_schema.dump(company), HTTPStatus.OK
    
    return '', HTTPStatus.NO_CONTENT