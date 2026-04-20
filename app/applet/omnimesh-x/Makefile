dev:
	cd src && uvicorn omnimesh_x.deployment.api_server:app --reload --port 8000

test:
	pytest tests/

install:
	pip install fastapi uvicorn pydantic pydantic-settings structlog
