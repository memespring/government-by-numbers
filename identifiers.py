import re

def is_unique_property_reference_number(subject):
    pattern = "^[0-9]{1,12}$"
    if re.match(pattern, subject):
        return True
    else:
        return False

def is_national_insurance_number(subject):
    pattern = "^\s*[a-zA-Z]{2}(?:\s*\d\s*){6}[a-zA-Z]?\s*$"
    if re.match(pattern, subject):
        return True
    else:
        return False

def is_unique_tax_reference(subject):
    pattern = "^[0-9]{10}$"
    if re.match(pattern, subject):
        return True
    else:
        return False

def is_passport_number(subject):
    pattern = "^[0-9]{9}$"
    if re.match(pattern, subject):
        return True
    else:
        return False

def is_land_title(subject):
    pattern = "^(AGL|BD|BGL|BK|BL|BM|CB|CE|CH|CL|CU|CYM|DN|DT|DU|DY|ESX|EX|GR|HD|HE|HP|HS|IW|K|LAN|LL|LT|MAN|MM|MS|ND|NGL|NK|NN|NT|NYK|ON|PM|SF|SGL|SH|SK|SL|ST|SY|SYK|TGL|TT|TY|WK|WR|WS|WSX|WT|YEA|YY)[0-9]*$"
    if re.match(pattern, subject):
        return True
    else:
        return False

def is_numberplate(subject):
    pattern = '^([A-Z]{3}\s?(\d{3}|\d{2}|d{1})\s?[A-Z])|([A-Z]\s?(\d{3}|\d{2}|\d{1})\s?[A-Z]{3})|(([A-HK-PRSVWY][A-HJ-PR-Y])\s?([0][2-9]|[1-9][0-9])\s?[A-HJ-PR-Z]{3})$'

    if re.match(pattern, subject):
        return True
    else:
        return False

def is_postcode(postcode):

    #See http://www.govtalk.gov.uk/gdsc/html/noframes/PostCode-2-1-Release.htm

    in_ = 'ABDEFGHJLNPQRSTUWXYZ';
    fst = 'ABCDEFGHIJKLMNOPRSTUWYZ';
    sec = 'ABCDEFGHJKLMNOPQRSTUVWXY';
    thd = 'ABCDEFGHJKSTUW';
    fth = 'ABEHMNPRVWXY';
    num = '0123456789';
    nom = '0123456789';
    gap = '\s\.';

    if re.findall("^[%s][%s][%s]*[%s][%s][%s]$" % (fst, num, gap, nom, in_, in_), postcode, re.IGNORECASE):
      return True
    elif re.findall("^[%s][%s][%s][%s]*[%s][%s][%s]$" % (fst, num, num, gap, nom, in_, in_), postcode, re.IGNORECASE):
      return True
    elif re.findall("^[%s][%s][%s][%s]*[%s][%s][%s]$" % (fst, sec, num, gap, nom, in_, in_), postcode, re.IGNORECASE):
      return True
    elif re.findall("^[%s][%s][%s][%s][%s]*[%s][%s][%s]$" % (fst, sec, num, num, gap, nom, in_, in_), postcode, re.IGNORECASE):
      return True
    elif re.findall("^[%s][%s][%s][%s]*[%s][%s][%s]$" % (fst, num, thd, gap, nom, in_, in_), postcode, re.IGNORECASE):
      return True
    elif re.findall("^[%s][%s][%s][%s][%s]*[%s][%s][%s]$" % (fst, sec, num, fth, gap, nom, in_, in_), postcode, re.IGNORECASE):
      return True
    else:
      return False
