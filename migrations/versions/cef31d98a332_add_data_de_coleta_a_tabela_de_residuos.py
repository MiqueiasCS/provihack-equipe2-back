"""add data de coleta a tabela de residuos

Revision ID: cef31d98a332
Revises: 827aad95311f
Create Date: 2022-04-29 21:02:19.793024
"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'cef31d98a332'
down_revision = '827aad95311f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('residues', sa.Column('date', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('residues', 'date')
    # ### end Alembic commands ###
