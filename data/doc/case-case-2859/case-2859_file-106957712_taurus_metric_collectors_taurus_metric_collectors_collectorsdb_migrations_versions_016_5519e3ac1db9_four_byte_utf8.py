"""four-byte-utf8

Revision ID: 5519e3ac1db9
Revises: 375d9de88cfd
Create Date: 2017-05-11 18:26:28.812089

"""

# revision identifiers, used by Alembic.
revision = '5519e3ac1db9'
down_revision = '375d9de88cfd'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql


def upgrade():
    # Change real_name and retweeted_real_name columns to 4-byte UTF8
    # to support embedded emoji
    op.alter_column('twitter_tweets', 'real_name',
                    type_=mysql.VARCHAR(
                        length=100,
                        charset="utf8mb4",
                        collation="utf8mb4_unicode_ci"),
                    existing_nullable=True)

    op.alter_column('twitter_tweets', 'retweeted_real_name',
                    type_=mysql.VARCHAR(
                        length=100,
                        charset="utf8mb4",
                        collation="utf8mb4_unicode_ci"),
                    existing_nullable=True,
                    existing_server_default="")


def downgrade():
    raise NotImplementedError("Rollback is not supported.")
