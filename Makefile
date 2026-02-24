PKG_NAME=justserpapi

.PHONY: init build clean check upload-test upload

init:
	python3 -m pip install --upgrade pip
	python3 -m pip install --upgrade build twine

clean:
	rm -rf build dist *.egg-info

build: clean
	python3 -m build

check:
	python3 -m twine check dist/*

upload-test: build check
	python3 -m twine upload --repository testpypi dist/*

upload: build check
	python3 -m twine upload dist/*
