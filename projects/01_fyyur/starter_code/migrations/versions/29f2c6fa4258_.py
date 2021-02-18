"""empty message

Revision ID: 29f2c6fa4258
Revises: a972fc55fc4c
Create Date: 2021-02-17 15:07:35.400972

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '29f2c6fa4258'
down_revision = 'a972fc55fc4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Shows', sa.Column('Venue_id', sa.Integer(), nullable=False))
    op.drop_constraint('Shows_venue_id_fkey', 'Shows', type_='foreignkey')
    op.create_foreign_key(None, 'Shows', 'Venue', ['Venue_id'], ['id'])
    op.drop_column('Shows', 'venue_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Shows', sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'Shows', type_='foreignkey')
    op.create_foreign_key('Shows_venue_id_fkey', 'Shows', 'Venue', ['venue_id'], ['id'])
    op.drop_column('Shows', 'Venue_id')
    # ### end Alembic commands ###