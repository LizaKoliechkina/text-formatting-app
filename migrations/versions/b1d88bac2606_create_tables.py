"""create tables

Revision ID: b1d88bac2606
Revises: 
Create Date: 2021-03-12 13:46:17.937027

"""
from alembic import op
import sqlalchemy as sa

from server.format import Filter

# revision identifiers, used by Alembic.
revision = 'b1d88bac2606'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'format_text',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('text', sa.String(), nullable=False),
        sa.Column('done', sa.Boolean(), default=False),
    )

    op.create_table(
        'history',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('text_id', sa.Integer(), sa.ForeignKey('format_text.id'), nullable=False),
        sa.Column('formatted', sa.String(), nullable=False),
        sa.Column('filter', sa.Enum(Filter), nullable=False),
        sa.Column('queue', sa.Integer(), nullable=False),
    )


def downgrade():
    op.drop_table('history')
    op.drop_table('format_text')
