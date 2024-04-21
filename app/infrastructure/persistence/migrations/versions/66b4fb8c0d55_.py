"""empty message

Revision ID: 66b4fb8c0d55
Revises:
Create Date: 2024-04-20 13:49:38.192159

"""

from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = "66b4fb8c0d55"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "hotels",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("services", postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.Column("rooms_quantity", sa.Integer(), nullable=False),
        sa.Column("image_id", sa.Integer(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_hotels_id"), "hotels", ["id"], unique=True)
    op.create_table(
        "users",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_users_id"), "users", ["id"], unique=True)
    op.create_table(
        "rooms",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("hotel_id", sa.UUID(), nullable=False),
        sa.Column("name", sa.String(), nullable=False),
        sa.Column("description", sa.String(), nullable=True),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column("services", postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("image_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(["hotel_id"], ["hotels.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_rooms_id"), "rooms", ["id"], unique=True)
    op.create_table(
        "bookings",
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("room_id", sa.UUID(), nullable=False),
        sa.Column("user_id", sa.UUID(), nullable=False),
        sa.Column("date_from", sa.Date(), nullable=False),
        sa.Column("date_to", sa.Date(), nullable=False),
        sa.Column("price", sa.Integer(), nullable=False),
        sa.Column(
            "total_cost",
            sa.Integer(),
            sa.Computed(
                "(date_to - date_from) * price",
            ),
            nullable=False,
        ),
        sa.Column(
            "total_days",
            sa.Integer(),
            sa.Computed(
                "date_to - date_from",
            ),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(["room_id"], ["rooms.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_bookings_id"), "bookings", ["id"], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_bookings_id"), table_name="bookings")
    op.drop_table("bookings")
    op.drop_index(op.f("ix_rooms_id"), table_name="rooms")
    op.drop_table("rooms")
    op.drop_index(op.f("ix_users_id"), table_name="users")
    op.drop_table("users")
    op.drop_index(op.f("ix_hotels_id"), table_name="hotels")
    op.drop_table("hotels")
    # ### end Alembic commands ###
