import sqlalchemy as sa

from workers_hierarchy.migrations import metadata


__all__ = ['workers', ]

workers = sa.Table(
    'workers', metadata,
    sa.Column('id', sa.Integer, primary_key=True, index=True),
    sa.Column('first_name', sa.String(200), nullable=False),
    sa.Column('surname', sa.String(200), nullable=False),
    sa.Column('last_name', sa.String(200), nullable=False),
    sa.Column('position', sa.String(200), nullable=False),
    sa.Column('salary', sa.Integer, nullable=False),
    sa.Column('employment_date', sa.Date, nullable=False),
    sa.Column('manager_id', sa.Integer, sa.ForeignKey("workers.id")),
    sa.UniqueConstraint('first_name', 'surname', 'last_name', name='const')
)
