from flask import Flask, request, redirect, render_template
import jinja2
import os
from identifiers import *

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():

    return render_template('index.html')

@app.route("/search", methods=['POST'])
def search():

    search_term = request.form.get('q', None)
    search_types = []

    if is_postcode(search_term):
        search_types.append('postcode')

    if is_unique_property_reference_number(search_term):
        search_types.append('unique property reference number')

    if is_land_title(search_term):
        search_types.append('land registry title')

    if is_numberplate(search_term):
        search_types.append('vehicle')

    if is_unique_tax_reference(search_term):
        search_types.append('tax reference number')

    if is_national_insurance_number(search_term):
        search_types.append('national insurance number')

    if is_passport_number(search_term):
        search_types.append('passport number')

    return render_template('results.html', search_types=search_types)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
