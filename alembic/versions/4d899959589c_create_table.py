"""create table

Revision ID: 4d899959589c
Revises: 
Create Date: 2023-01-25 15:00:05.133873

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d899959589c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('name_server', sa.Integer(), nullable=False),
                    sa.Column('name_user', sa.Text(), nullable=False),
                    sa.Column('count', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
    op.drop_table('users')
