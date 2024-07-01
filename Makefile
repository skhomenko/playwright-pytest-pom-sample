# variables
IMAGE_NAME = playwright-tests

# Default target
.PHONY: all
all: build run-all-tests

# Build the Docker image
.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

# Run all chromium tests in the Docker container
.PHONY: run-run-all-chromium-tests-tests
run-all-chromium-tests:
	docker run --rm -e BROWSER=chromium $(IMAGE_NAME)

# Run all firefox tests in the Docker container
.PHONY: run-run-all-firefox-tests-tests
run-all-firefox-tests:
	docker run --rm -e BROWSER=firefox  $(IMAGE_NAME)

# Run all tests in both Chromium and Firefox
.PHONY: run-all-tests
run-all-tests: run-all-chromium-tests run-all-firefox-tests
