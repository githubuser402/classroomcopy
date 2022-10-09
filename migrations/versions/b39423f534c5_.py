"""empty message

Revision ID: b39423f534c5
Revises: 5f1918c30423
Create Date: 2022-10-09 23:19:48.890477

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b39423f534c5'
down_revision = '5f1918c30423'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('slug_id', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'slug_id')
    # ### end Alembic commands ###
