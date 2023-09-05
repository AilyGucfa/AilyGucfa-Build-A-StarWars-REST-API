"""empty message

Revision ID: 978d2fb6d21f
Revises: 72f0a40f2d09
Create Date: 2023-09-05 06:27:12.504912

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '978d2fb6d21f'
down_revision = '72f0a40f2d09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('favorite',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('item_type', sa.String(length=50), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favorite')
    # ### end Alembic commands ###
