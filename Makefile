VENV := venv
PACKAGE := sim

all: venv

# setup virtual env
$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# activate virtual env
venv: $(VENV)/bin/activate

# runs the main package
run: venv
	./$(VENV)/bin/python3 -m $(PACKAGE)

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean
