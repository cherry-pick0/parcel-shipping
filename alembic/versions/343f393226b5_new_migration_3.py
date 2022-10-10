"""New Migration 3

Revision ID: 343f393226b5
Revises: b2c0eceb2fb0
Create Date: 2022-10-10 17:44:43.485479

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '343f393226b5'
down_revision = 'b2c0eceb2fb0'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'package', ['id'])
    op.create_unique_constraint(None, 'recipient', ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipient', type_='unique')
    op.drop_constraint(None, 'package', type_='unique')
    # ### end Alembic commands ###
