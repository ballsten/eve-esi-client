VENV = venv
PYTHON = py

.PHONY = init clean generate test

# install requirements.txt & test-requirements.txt
init: $(VENV)/scripts/activate requirements.txt
	$(VENV)/scripts/pip install -r requirements.txt
	$(VENV)/scripts/pip install -r test-requirements.txt

# create venv direcotry
# upgrade pip
$(VENV)/scripts/activate:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/scripts/python -m pip install --upgrade pip

# generate openapi client
generate:
	openapi-generator-cli generate -c generate.yaml


# run tests
test:
	pytest
	
# remove venv directory
clean:
	rm -rf $(VENV)