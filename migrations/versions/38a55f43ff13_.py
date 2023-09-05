"""empty message

Revision ID: 38a55f43ff13
Revises: a9162d67272e
Create Date: 2023-09-02 00:41:08.857722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38a55f43ff13'
down_revision = 'a9162d67272e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vehicles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('vehicle_name', sa.String(length=30), nullable=False),
    sa.Column('model', sa.String(length=30), nullable=True),
    sa.Column('vehicle_class', sa.String(length=30), nullable=True),
    sa.Column('manufacturer', sa.String(length=30), nullable=True),
    sa.Column('cost_in_credits', sa.String(length=30), nullable=True),
    sa.Column('lenght', sa.String(length=30), nullable=True),
    sa.Column('crew', sa.String(length=30), nullable=True),
    sa.Column('passengers', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vehicles')
    # ### end Alembic commands ###