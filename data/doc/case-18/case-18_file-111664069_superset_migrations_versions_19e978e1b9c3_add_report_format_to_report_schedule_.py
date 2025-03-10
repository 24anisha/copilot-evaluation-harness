# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""add_report_format_to_report_schedule_model.py

Revision ID: 19e978e1b9c3
Revises: fc3a3a8ff221
Create Date: 2021-04-06 21:39:52.259223

"""

# revision identifiers, used by Alembic.
revision = "19e978e1b9c3"
down_revision = "fc3a3a8ff221"

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql


def upgrade():
    op.add_column(
        "report_schedule",
        sa.Column(
            "report_format", sa.String(length=50), server_default="PNG", nullable=True
        ),
    )


def downgrade():
    op.drop_column("report_schedule", "report_format")