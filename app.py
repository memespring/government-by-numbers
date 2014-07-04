from flask import Flask, request, redirect, render_template
import jinja2
import os
from identifiers import *
import govuk

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():

    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():

    search_term = request.form.get('q', None)
    search_type = 'unknown'
    standard_results = []

    if is_postcode(search_term):
        search_type = 'postcode'
    elif is_land_title(search_term):
        search_type = 'land registry title'
    elif is_numberplate(search_term):
        search_type = 'vehicle'
    elif is_unique_tax_reference(search_term):
        search_type = 'tax reference number'
        standard_results = govuk.search('Self Assessment')
    elif is_national_insurance_number(search_term):
        search_type = 'national insurance number'
    elif is_passport_number(search_term):
        search_type = 'passport number'
        standard_results = govuk.search('passport')

    return render_template('results.html', search_type=search_type, standard_results=standard_results)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
