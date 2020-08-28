"""empty message

Revision ID: 74f9f2114d34
Revises: 66cb93a66d6b
Create Date: 2020-08-28 18:08:56.315034

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74f9f2114d34'
down_revision = '66cb93a66d6b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('neibour_echo_key', 'neibour', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('neibour_echo_key', 'neibour', ['echo'])
    # ### end Alembic commands ###
