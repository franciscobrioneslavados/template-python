from typing import Any

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from container import ApplicationContainer
from infrastructure.api.todo import controller as todoController


def setup(app: FastAPI, container: ApplicationContainer) -> None:

    # Add other controllers here
    app.include_router(todoController.router)

    # Inject dependencies
    container.wire(
        modules=[
            todoController,
        ]
    )

    # Customize the openAPI documentation
    def custom_openapi() -> Any:
        if app.openapi_schema:
            return app.openapi_schema
        openapi_schema = get_openapi(
            title="My TODO app",
            # version=__version__,
            version="0.0.1",
            description="My TODO app API'",
            routes=app.routes,
        )
        if not container.configuration.api_prefix():
            openapi_schema["servers"] = [{"url": "/"}]
        else:
            openapi_schema["servers"] = [{"url": container.configuration.api_prefix()}]
        app.openapi_schema = openapi_schema
        return app.openapi_schema

    app.openapi = custom_openapi