"""create posts table

Revision ID: 500a99e82656
Revises: 
Create Date: 2022-06-22 14:26:49.837105

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '500a99e82656'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.INTEGER(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
