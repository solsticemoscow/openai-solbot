"""add all

Revision ID: f1bc1d4477da
Revises: 
Create Date: 2024-06-05 13:28:08.402393

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1bc1d4477da'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Admin',
    sa.Column('id', sa.String(length=100), nullable=False),
    sa.Column('captcha', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('Users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('username', sa.String(length=200), nullable=True),
    sa.Column('firstname', sa.String(length=200), nullable=True),
    sa.Column('lastname', sa.String(length=200), nullable=True),
    sa.Column('language_code', sa.String(length=20), nullable=True),
    sa.Column('profile_description', sa.Text(), nullable=True),
    sa.Column('time_added', sa.DateTime(), nullable=True),
    sa.Column('blocked', sa.Boolean(), nullable=True),
    sa.Column('captcha', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Users')
    op.drop_table('Admin')
    # ### end Alembic commands ###
