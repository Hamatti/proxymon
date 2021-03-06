import os
from flask import Flask, render_template, request, flash
from models.ptcgoparser import PTCGOParser

app = Flask(__name__)
app.use_reloader=False
app.debug=False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/proxies')
def proxies():
    return render_template('proxies.html')

@app.route('/featured/<deckname>/')
def featured(deckname):
    return render_template('featured/%s.html' % deckname)

@app.route('/generate', methods=['POST'])
def generate_from_decklist():
    decklist = request.form['decklist']

    p = PTCGOParser(decklist)
    p.run()
    return p.full_html

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
