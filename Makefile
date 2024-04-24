style:
	poetry run black src/
	poetry run flake8 src/
	poetry run pylint src/