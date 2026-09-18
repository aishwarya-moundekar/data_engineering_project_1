"""create network_nodes

Revision ID: f9c2bc281b5b
Revises: cfd859ad1360
Create Date: 2026-09-17 17:03:19.570580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry

# revision identifiers, used by Alembic.
revision: str = 'f9c2bc281b5b'
down_revision: Union[str, Sequence[str], None] = 'cfd859ad1360'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "network_nodes",
        sa.Column("node_id", sa.BigInteger(), autoincrement=True, nullable=False),
        sa.Column("node_code", sa.String(length=50), nullable=False),
        sa.Column("node_name", sa.String(length=150), nullable=False),
        sa.Column("node_type", sa.String(length=50), nullable=False),
        sa.Column("status", sa.String(length=30), nullable=False),
        sa.Column("provider", sa.String(length=100), nullable=True),
        sa.Column("capacity_gbps", sa.Numeric(10, 2), nullable=True),
        sa.Column("latitude", sa.Numeric(9, 6), nullable=False),
        sa.Column("longitude", sa.Numeric(9, 6), nullable=False),
        sa.Column(
            "location",
            Geometry(geometry_type="POINT", srid=4326),
            nullable=False
        ),
        sa.Column("coverage_radius_km", sa.Numeric(8, 2), nullable=True),
        sa.Column("elevation_m", sa.Numeric(8, 2), nullable=True),
        sa.Column("city", sa.String(length=100), nullable=True),
        sa.Column("country", sa.String(length=100), nullable=True),
        sa.Column("installed_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("node_id"),
        sa.UniqueConstraint("node_code"),
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("network_nodes")

