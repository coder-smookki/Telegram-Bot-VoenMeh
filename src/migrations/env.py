import asyncio
import os
from logging.config import fileConfig

from alembic import context
from alembic.script import ScriptDirectory
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from database.models import *  # noqa: F403
from database.models.base import AlchemyBaseModel

config = context.config

section = config.config_ini_section
config.set_section_option(section, "POSTGRES_HOST", os.environ["POSTGRES_HOST"])
config.set_section_option(
    section, "POSTGRES_HOST_PORT", os.environ["POSTGRES_HOST_PORT"]
)
config.set_section_option(section, "POSTGRES_DB", os.environ["POSTGRES_DB"])
config.set_section_option(section, "POSTGRES_USER", os.environ["POSTGRES_USER"])
config.set_section_option(section, "POSTGRES_PASSWORD", os.environ["POSTGRES_PASSWORD"])

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = AlchemyBaseModel.metadata


def process_revision_directives(context, revision, directives):
    migration_script = directives[0]
    head_revision = ScriptDirectory.from_config(context.config).get_current_head()

    if head_revision is None:
        new_rev_id = 1
    else:
        last_rev_id = int(head_revision.lstrip("0"))
        new_rev_id = last_rev_id + 1
    migration_script.rev_id = f"{new_rev_id:04}"


def run_migrations_offline() -> None:

    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        process_revision_directives=process_revision_directives,
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(
        connection=connection,
        target_metadata=target_metadata,
        process_revision_directives=process_revision_directives,
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:

    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:

    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()