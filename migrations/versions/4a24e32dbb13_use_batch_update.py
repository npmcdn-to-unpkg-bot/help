"""use batch update

Revision ID: 4a24e32dbb13
Revises: 6c69768c0d86
Create Date: 2016-07-23 08:06:50.787916

"""

# revision identifiers, used by Alembic.
revision = '4a24e32dbb13'
down_revision = '6c69768c0d86'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modules', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(length=60),
               type_=sa.String(length=255),
               existing_nullable=True)

    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('modules', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.String(length=255),
               type_=sa.VARCHAR(length=60),
               existing_nullable=True)

    ### end Alembic commands ###
