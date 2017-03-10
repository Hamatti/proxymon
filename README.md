#Proxymon
## Your #1 Source for PTCG Proxy Decks

Proxymon is a hobby project built to help Pokemon TCG players test out new decks and combinations faster.

Test it out at [https://proxymon.herokuapp.com](https://proxymon.herokuapp.com)

## Installation

```
$ git clone https://github.com/Hamatti/proxymon.git
$ cd proxymon
$ export FLASK_APP=app.py
$ virtualenv .venv
$ source .venv/bin/activate
$ pip install -r requirements
$ cd utils
$ ./load_cards.sh
$ python cards.py
$ cd ..
$ flask run
```

