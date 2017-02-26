import os
from flask import Flask, render_template, request
from ptcgo import PTCGOParser

app = Flask(__name__)
app.use_reloader=False
app.debug=False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_from_decklist():
    decklist = request.form['decklist']
    decklist_format = request.form['deckformat']
    if decklist_format == 'ptcgo':
        parser = PTCGOParser

    p = parser(decklist)
    p.run()
    return p.full_html

port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
