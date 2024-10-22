"""empty message

Revision ID: b7179a870f7e
Revises: 66b4fb8c0d55
Create Date: 2024-04-21 15:47:39.580225

"""

from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b7179a870f7e"
down_revision: str | None = "66b4fb8c0d55"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint("unique_name_location", "hotels", ["name", "location"])
    op.create_unique_constraint("unique_room_hotel_id", "rooms", ["name", "hotel_id"])
    op.create_unique_constraint(None, "users", ["email"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "users", type_="unique")
    op.drop_constraint("unique_room_hotel_id", "rooms", type_="unique")
    op.drop_constraint("unique_name_location", "hotels", type_="unique")
    # ### end Alembic commands ###
