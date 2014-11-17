"""Add watchers to polls

Revision ID: 54ef64095b17
Revises: 44fde7756d60
Create Date: 2014-11-17 15:29:20.564779

"""

# revision identifiers, used by Alembic.
revision = '54ef64095b17'
down_revision = '44fde7756d60'

from alembic import op
import sqlalchemy as sa

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('poll_watch',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('poll_id', sa.INTEGER(), nullable=True),
    sa.Column('user_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['poll_id'], [u'poll.id'], ),
    sa.ForeignKeyConstraint(['user_id'], [u'user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###

def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('poll_watch')
    ### end Alembic commands ###

