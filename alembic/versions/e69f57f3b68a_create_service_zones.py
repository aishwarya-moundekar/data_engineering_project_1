"""create service_zones

Revision ID: e69f57f3b68a
Revises: aa282bfa2aae
Create Date: 2026-09-18 15:55:51.338557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry


# revision identifiers, used by Alembic.
revision: str = 'e69f57f3b68a'
down_revision: Union[str, Sequence[str], None] = 'aa282bfa2aae'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_table(
        "service_zones",

        sa.Column(
            "zone_id",
            sa.BigInteger(),
            autoincrement=True,
            nullable=False
        ),
        sa.Column(
            "zone_code",
            sa.String(length=50),
            nullable=False
        ),
        sa.Column(
            "zone_name",
            sa.String(length=150),
            nullable=False
        ),
        sa.Column(
            "zone_type",
            sa.String(length=50),
            nullable=False
        ),
        sa.Column(
            "priority",
            sa.String(length=20),
            nullable=False
        ),
        sa.Column(
            "city",
            sa.String(length=100),
            nullable=True
        ),
        sa.Column(
            "country",
            sa.String(length=100),
            nullable=True
        ),
        sa.Column(
            "population",
            sa.BigInteger(),
            nullable=True
        ),
        sa.Column(
            "households",
            sa.BigInteger(),
            nullable=True
        ),
        sa.Column(
            "avg_download_mbps",
            sa.Numeric(10, 2),
            nullable=True
        ),
        sa.Column(
            "avg_upload_mbps",
            sa.Numeric(10, 2),
            nullable=True
        ),
        sa.Column(
            "target_download_mbps",
            sa.Numeric(10, 2),
            nullable=True
        ),
        sa.Column(
            "coverage_target_pct",
            sa.Numeric(5, 2),
            nullable=True
        ),
        sa.Column(
            "boundary",
            Geometry(
                geometry_type="MULTIPOLYGON",
                srid=4326
            ),
            nullable=False
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

        sa.PrimaryKeyConstraint("zone_id"),
        sa.UniqueConstraint("zone_code"),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_table("service_zones")