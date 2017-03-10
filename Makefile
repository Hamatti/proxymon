install:
	venv/bin/pip install -r requirements.txt

build:
	./utils/load_cards.sh
	venv/bin/python utils/combine_sets.py
