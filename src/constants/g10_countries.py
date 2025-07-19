"""
Constants for G10 countries.
"""

# G10 countries mapped to their information.
G10_COUNTRIES = {
    "Belgium": {"code": "BE"},
    "Canada": {"code": "CA"},
    "Switzerland": {"code": "CH"},
    "Denmark": {"code": "DE"},
    "France": {"code": "FR"},
    "United Kingdom": {"code": "GB"},
    "Italy": {"code": "IT"},
    "Japan": {"code": "JP"},
    "Netherlands": {"code": "NL"},
    "Sweden": {"code": "SE"},
    "United States": {"code": "US"}
}

# G10 country codes mapped to their country names.
CODE_TO_COUNTRY = {v["code"]: k for k, v in G10_COUNTRIES.items()}