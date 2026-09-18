"""create network_links

Revision ID: aa282bfa2aae
Revises: f9c2bc281b5b
Create Date: 2026-09-18 14:58:13.832109

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision: str = 'aa282bfa2aae'
down_revision: Union[str, Sequence[str], None] = 'f9c2bc281b5b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "network_links",

        sa.Column(
            "link_id",
            sa.BigInteger(),
            autoincrement=True,
            nullable=False
        ),

        sa.Column(
            "link_code",
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            "source_node_id",
            sa.BigInteger(),
            nullable=False
        ),

        sa.Column(
            "target_node_id",
            sa.BigInteger(),
            nullable=False
        ),

        sa.Column(
            "link_type",
            sa.String(length=50),
            nullable=False
        ),

        sa.Column(
            "status",
            sa.String(length=30),
            nullable=False
        ),

        sa.Column(
            "bandwidth_gbps",
            sa.Numeric(10, 2),
            nullable=True
        ),

        sa.Column(
            "latency_ms",
            sa.Numeric(10, 2),
            nullable=True
        ),

        sa.Column(
            "distance_km",
            sa.Numeric(12, 3),
            nullable=True
        ),

        sa.Column(
            "reliability_pct",
            sa.Numeric(5, 2),
            nullable=True
        ),

        sa.Column(
            "source_location",
            Geometry(
                geometry_type="POINT",
                srid=4326
            ),
            nullable=True
        ),

        sa.Column(
            "target_location",
            Geometry(
                geometry_type="POINT",
                srid=4326
            ),
            nullable=True
        ),

        sa.Column(
            "route",
            Geometry(
                geometry_type="LINESTRING",
                srid=4326
            ),
            nullable=True
        ),

        sa.Column(
            "city",
            sa.String(length=100),
            nullable=True
        ),

        sa.Column(
            "created_at",
            sa.DateTime(),
            nullable=False
        ),

        sa.Column(
            "updated_at",
            sa.DateTime(),
            nullable=False
        ),

        sa.PrimaryKeyConstraint("link_id"),

        sa.UniqueConstraint("link_code"),

        sa.ForeignKeyConstraint(
            ["source_node_id"],
            ["network_nodes.node_id"]
        ),

        sa.ForeignKeyConstraint(
            ["target_node_id"],
            ["network_nodes.node_id"]
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table("network_links")