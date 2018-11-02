JSON = movies.jsons
QUERY = query.sparql
PLOTS = plots.json

VENV = venv
REQUIREMENTS = requirements.txt
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
DEPS = $(VENV)/.deps

SCRIPT = movies_durations.py

$(JSON): $(QUERY)
	curl -G https://query.wikidata.org/bigdata/namespace/wdq/sparql \
		--data-urlencode query@$< -d format=json > $@

$(VENV):
	virtualenv --python python3 $@

$(DEPS): $(VENV) $(REQUIREMENTS)
	$(PIP) install -r $(REQUIREMENTS)
	touch $@

$(PLOTS): $(DEPS) $(JSON) $(SCRIPT)
	$(PYTHON) $(SCRIPT) --file $(JSON) --output $@
