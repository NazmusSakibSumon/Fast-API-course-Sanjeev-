"""add foreign-key to posts table

Revision ID: 9a694c1858fb
Revises: c82c1e9b97e1
Create Date: 2022-06-22 15:22:04.593724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a694c1858fb'
down_revision = 'c82c1e9b97e1'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts','owner_id')
    pass
