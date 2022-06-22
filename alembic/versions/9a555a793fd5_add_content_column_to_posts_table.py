"""add content column to posts table

Revision ID: 9a555a793fd5
Revises: 500a99e82656
Create Date: 2022-06-22 14:47:14.284758

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a555a793fd5'
down_revision = '500a99e82656'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts','content')
    pass
