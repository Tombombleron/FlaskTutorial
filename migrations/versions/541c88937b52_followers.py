"""followers

Revision ID: 541c88937b52
Revises: 3b16280addfc
Create Date: 2018-04-23 20:30:07.526873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '541c88937b52'
down_revision = '3b16280addfc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###