"""empty message

Revision ID: be83d15908dd
Revises: 4a7b1bf9e0fc
Create Date: 2018-07-29 18:59:44.069196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'be83d15908dd'
down_revision = '4a7b1bf9e0fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('is_veep_x', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'is_veep_x')
    # ### end Alembic commands ###