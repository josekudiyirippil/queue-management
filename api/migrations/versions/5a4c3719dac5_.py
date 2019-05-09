"""empty message

Revision ID: 5a4c3719dac5
Revises: 52a334670eb7
Create Date: 2018-11-09 19:18:06.999522

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a4c3719dac5'
down_revision = '52a334670eb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('citizen', sa.Column('priority', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('citizen', 'priority')
    # ### end Alembic commands ###