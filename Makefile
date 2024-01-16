VENV = venv # name of venv directory
PYTHON = py # python version to use to create venv

.PHONY = init clean generate test

# install requirements.txt & test-requirements.txt
init: $(VENV)/scripts/activate requirements.txt
	$(VENV)/scripts/pip -r requirements.txt
	$(VENV)/scripts/pip -r test-requirements.txt

# create venv direcotry
# upgrade pip
$(VENV)/scripts/activate:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/scripts/python -m pip --upgrade pip

# generate openapi client
generate:
	openapi-generator-cli generate -c generate.yaml
	
# remove venv directory
clean:
	rm -rf $(VENV)