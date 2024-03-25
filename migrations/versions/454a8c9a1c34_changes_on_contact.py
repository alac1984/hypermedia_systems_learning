"""Changes on Contact

Revision ID: 454a8c9a1c34
Revises: e89377edfbf9
Create Date: 2024-03-19 15:03:05.156806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = "454a8c9a1c34"
down_revision: Union[str, None] = "e89377edfbf9"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("contact", "gender", existing_type=sa.VARCHAR(), nullable=True)
    # op.create_index('idx_contact_first_name', 'contact', ['first_name'], unique=False, postgresql_using='gin')
    op.create_index(
        "idx_contact_first_name",
        "contact",
        [sa.text("first_name gin_trgm_ops")],
        unique=False,
        postgresql_using="gin",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        "idx_contact_first_name", table_name="contact", postgresql_using="gin"
    )
    op.alter_column("contact", "gender", existing_type=sa.VARCHAR(), nullable=False)
    # ### end Alembic commands ###