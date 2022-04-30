from http import HTTPStatus

from app.models.residue_model import ResidueGetSchema, ResidueModel
from app.services.exceptions import Not_found_item_error


def retrieve_residues():
    residue_schema = ResidueGetSchema()
    residues = ResidueModel.query.all()

    return residue_schema.dumps(residues, many=True), HTTPStatus.OK


def retrieve_one_residue(uuid):
    residue_schema = ResidueGetSchema()
    try:
        residue = ResidueModel.query.get(uuid)

        if not residue:
            raise Not_found_item_error('Residuo nao encontrado')

    except Not_found_item_error as err:
        return {'message': err.message}, HTTPStatus.NOT_FOUND

    return residue_schema.dump(residue)
