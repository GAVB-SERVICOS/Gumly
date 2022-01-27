SRC_FOLDER=rico
TEST_FOLDER=tests

# we mark all commands as `phony` to avoid any potential conflict with files in the CICD environment
.PHONY: lint format isort typecheck typecheck verify build

lint:
	flake8 --exit-zero $(SRC_FOLDER)

format:
	black --verbose $(SRC_FOLDER) $(TEST_FOLDER)

isort:
	isort $(SRC_FOLDER) $(TEST_FOLDER)

typecheck:
	mypy --namespace-packages --explicit-package-bases -p rico
	mypy --namespace-packages tests

test:
	pytest --durations=5 $(TEST_FOLDER)

cov:
	pytest --cov=rico --durations=5 $(TEST_FOLDER)

verify: lint typecheck test
	echo "Lint, typecheck, test successfully completed!"

build:
	python -m build --sdist --wheel --outdir dist/ .
