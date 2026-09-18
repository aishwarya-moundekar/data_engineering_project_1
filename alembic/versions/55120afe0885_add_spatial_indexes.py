"""add spatial indexes

Revision ID: 55120afe0885
Revises: e69f57f3b68a
Create Date: 2026-09-18 16:28:32.379200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '55120afe0885'
down_revision: Union[str, Sequence[str], None] = 'e69f57f3b68a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.execute("""
        CREATE INDEX IF NOT EXISTS idx_network_nodes_location
        ON network_nodes
        USING GIST(location);
    """)

    op.execute("""
        CREATE INDEX IF NOT EXISTS idx_network_links_source_location
        ON network_links
        USING GIST(source_location);
    """)

    op.execute("""
        CREATE INDEX IF NOT EXISTS idx_network_links_target_location
        ON network_links
        USING GIST(target_location);
    """)

    op.execute("""
        CREATE INDEX IF NOT EXISTS idx_network_links_route
        ON network_links
        USING GIST(route);
    """)

    op.execute("""
        CREATE INDEX IF NOT EXISTS idx_service_zones_boundary
        ON service_zones
        USING GIST(boundary);
    """)

def downgrade() -> None:
    """Downgrade schema."""

    op.execute("""
        DROP INDEX IF EXISTS idx_service_zones_boundary;
    """)

    op.execute("""
        DROP INDEX IF EXISTS idx_network_links_route;
    """)

    op.execute("""
        DROP INDEX IF EXISTS idx_network_links_target_location;
    """)

    op.execute("""
        DROP INDEX IF EXISTS idx_network_links_source_location;
    """)

    op.execute("""
        DROP INDEX IF EXISTS idx_network_nodes_location;
    """)

    