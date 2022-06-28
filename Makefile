.PHONY: run format

run:
	gunicorn -k uvicorn.workers.UvicornWorker -c gunicorn.py lunch.main:app --reload

format:
	flake8 .
	black .
	isort .
