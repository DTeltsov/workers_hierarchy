"""empty message

Revision ID: 15c6c9543c20
Revises: 
Create Date: 2022-10-26 08:57:37.546701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15c6c9543c20'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('workers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=200), nullable=False),
    sa.Column('surname', sa.String(length=200), nullable=False),
    sa.Column('last_name', sa.String(length=200), nullable=False),
    sa.Column('position', sa.String(length=200), nullable=False),
    sa.Column('salary', sa.Integer(), nullable=False),
    sa.Column('employment_date', sa.Date(), nullable=False),
    sa.Column('manager_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['manager_id'], ['workers.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('first_name', 'surname', 'last_name', name='const')
    )
    op.create_index(op.f('ix_workers_id'), 'workers', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_workers_id'), table_name='workers')
    op.drop_table('workers')
    # ### end Alembic commands ###
