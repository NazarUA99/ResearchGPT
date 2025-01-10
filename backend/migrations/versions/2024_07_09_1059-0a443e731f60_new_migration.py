"""new migration

Revision ID: 0a443e731f60
Revises: 
Create Date: 2024-07-09 10:59:00.377529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '0a443e731f60'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('reports',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('uuid', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('report_objective', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('report_target_audience', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('report_additional_information', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('report_content', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('report_citations', sa.JSON(), nullable=True),
    sa.Column('chunk_ids', sa.JSON(), nullable=True),
    sa.Column('tenant_id', sqlmodel.sql.sqltypes.GUID(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_index(op.f('ix_reports_uuid'), 'reports', ['uuid'], unique=False)
    op.create_table('chunks',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('uuid', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('query', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('llm_similarity_score', sa.Float(), nullable=True),
    sa.Column('vector_similarity_score', sa.Float(), nullable=True),
    sa.Column('source', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('content', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('captions_text', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('captions_highlights', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('report_id', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.ForeignKeyConstraint(['report_id'], ['reports.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_index(op.f('ix_chunks_uuid'), 'chunks', ['uuid'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_chunks_uuid'), table_name='chunks')
    op.drop_table('chunks')
    op.drop_index(op.f('ix_reports_uuid'), table_name='reports')
    op.drop_table('reports')
    # ### end Alembic commands ###
