"""empty message

Revision ID: 92cd814a5c05
Revises: 129ea023f600
Create Date: 2019-10-22 16:31:58.046195

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utc
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '92cd814a5c05'
down_revision = '129ea023f600'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('appointment', sa.Column('citizen_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'appointment', 'citizen', ['citizen_id'], ['citizen_id'])

    #  Insert a record into the citizen state table.
    op.execute("INSERT INTO citizenstate (cs_state_name, cs_state_desc) VALUES ('Appointment booked', 'Citizen has booked an appointment')")
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('appointment', 'citizen_id')

    #  Delete the Appointment booked record from the citizen state table.
    op.execute("DELETE FROM citizenstate where cs_state_name = 'Appointment booked'")
    # ### end Alembic commands ###
