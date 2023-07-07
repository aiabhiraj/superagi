"""create_agent_scheduler

Revision ID: ba60b12ae109
Revises: 83424de1347e
Create Date: 2023-07-04 10:58:37.991063

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ba60b12ae109'
down_revision = '83424de1347e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('agent_schedule',
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('agent_id', sa.Integer(), nullable=True),
    sa.Column('start_time', sa.DateTime(), nullable=True),
    sa.Column('next_scheduled_time', sa.DateTime(), nullable=True),
    sa.Column('recurrence_interval', sa.String(), nullable=True),
    sa.Column('expiry_date', sa.DateTime(), nullable=True),
    sa.Column('expiry_runs', sa.Integer(), nullable=True),
    sa.Column('current_runs', sa.Integer(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_agent_schedule_expiry_date'), 'agent_schedule', ['expiry_date'], unique=False)
    op.create_index(op.f('ix_agent_schedule_status'), 'agent_schedule', ['status'], unique=False)
    op.create_index(op.f('ix_agent_schedule_agent_id'), 'agent_schedule', ['agent_id'], unique=False)
    # ### end Alembic commands ###

    
def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_agent_schedule_agent_id'), table_name='agent_schedule')
    op.drop_index(op.f('ix_agent_schedule_status'), table_name='agent_schedule')
    op.drop_index(op.f('ix_agent_schedule_expiry_date'), table_name='agent_schedule')
    op.drop_table('agent_schedule')
    # ### end Alembic commands ###