from dependency_injector import providers, containers

from application.todo.service import TodoService
from infrastructure.database.todo_repository import (
    TodoEntryPickleRepository,
)


class ApplicationContainer(containers.DeclarativeContainer):
    configuration = providers.Configuration()

    todo_entry_repository = providers.Singleton(
        TodoEntryPickleRepository, storage_dir=configuration.storage_dir
    )

    todo_service = providers.Factory(TodoService, todo_entry_repository)