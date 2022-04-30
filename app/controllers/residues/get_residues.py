from http import HTTPStatus

from app.models.residue_model import ResidueGetSchema,ResidueModel


def retrieve_residues():
    residue_schema = ResidueGetSchema()
    residues = ResidueModel.query.all()

    return residue_schema.dumps(residues,many=True), HTTPStatus.OK


def retrieve_one_residue(uuid):
    residue_schema = ResidueGetSchema()

    residue = ResidueModel.query.get(uuid)
    print("*"*50)
    print(residue)
    return residue_schema.dump(residue)