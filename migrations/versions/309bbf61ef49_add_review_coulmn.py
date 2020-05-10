"""add review coulmn

Revision ID: 309bbf61ef49
Revises: c57b61c0ff73
Create Date: 2020-05-10 06:02:44.835031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '309bbf61ef49'
down_revision = 'c57b61c0ff73'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('review', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('review', 'review')
    # ### end Alembic commands ###