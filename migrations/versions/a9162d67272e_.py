"""empty message

Revision ID: a9162d67272e
Revises: ce6e23b4a668
Create Date: 2023-09-02 00:32:20.667883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9162d67272e'
down_revision = 'ce6e23b4a668'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('planet_name', sa.String(length=30), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('planets', schema=None) as batch_op:
        batch_op.drop_column('planet_name')

    # ### end Alembic commands ###
