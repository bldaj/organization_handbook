import asyncio
from logging.config import (
    fileConfig,
)

from alembic import (
    context,
)

from app.db.base import (
    Base,
)
from app.db.session import (
    DATABASE_URI,
    engine,
)
from app.model_registry import (
    autodiscover_models,
)


# Alembic Config object
config = context.config
fileConfig(config.config_file_name)

# Импортируем все модели
autodiscover_models()

# Метаданные
target_metadata = Base.metadata


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = DATABASE_URI
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""

    connectable = engine

    async def do_run_migrations():
        async with connectable.connect() as connection:
            await connection.run_sync(
                lambda sync_conn: context.configure(connection=sync_conn, target_metadata=target_metadata)
            )
            await connection.run_sync(lambda sync_conn: context.run_migrations())

    asyncio.run(do_run_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
