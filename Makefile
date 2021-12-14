all: \
	clean \
	init \
	test \
	doc


init:
	@pip \
		install \
		-r requirements.txt


doc:
	@nox \
		-s \
			docs


test:
	@nox \
		-s \
			tests


lint:
	@nox \
		-s \
			lint


clean:
	@rm -rf \
		.pytest_cache \
		.nox \
		.coverage \
		__pycache__ \
		tests/__pycache__


.PHONY: all init doc test lint clean
