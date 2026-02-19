"""Schema added in database table

Revision ID: fbf661eb1de4
Revises: 9f8ef78c6280
Create Date: 2026-01-02 16:39:24.167010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fbf661eb1de4'
down_revision: Union[str, Sequence[str], None] = '9f8ef78c6280'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
