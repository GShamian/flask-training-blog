"""empty message

Revision ID: a83637a3d1b3
Revises: 933869f1f224
Create Date: 2020-07-30 16:37:30.311838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a83637a3d1b3'
down_revision = '933869f1f224'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'tag', ['slug'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'tag', type_='unique')
    # ### end Alembic commands ###
