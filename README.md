# Template Python
#### A Python Template to run local with a Clean Architecture frameworks

### Create a virtual ENV 
```
python3 -m venv venv
source venv/bin/activate
```

### Install Python Management, see [Poetry Manager](https://python-poetry.org/) as init a proyect
```
pip install poetry
poetry init
```

### Adding Dependencies
poetry add dependency_injector
poetry add fastapi
poetry add uvicorn
poetry add pytest

### Adding DEV Dependencies
```
poetry add --dev  bandit
```

### RUN Server
```
poetry run python app/app.py
```

### Server run's on http://0.0.0.0:8080

### Swagger run's on http://0.0.0.0:8080/docs