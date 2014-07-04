# Government by numbers

A validator for various UK government identifiers

So far:

 * Postcode
 * Land Registry Title ID
 * number plate
 * Unique Tax Reference Number
 * National Insurance number
 * Passport Number
 * Unique  Property Reference Number


 ## Running locally

 Assuming you have pip and virtualenv installed:

 1. Clone this repo
 2. Create a virtualenv

```
     $ cd government-by-numbers
     $ virtualenv .
     $ source bin/activate
```

 3. Install requirements

 ```
     $ pip install -r requirements.txt
```
 4. Run

 ```
     $ python app.py
```

## Adding new numbers

Look in app.py
