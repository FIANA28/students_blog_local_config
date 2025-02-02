"""empty message

Revision ID: 1352cdc4a1dd
Revises: 10c6d4ffe45e
Create Date: 2020-12-07 13:55:26.874258

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1352cdc4a1dd'
down_revision = '10c6d4ffe45e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
