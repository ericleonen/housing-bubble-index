"""
Configurations for data sources.
"""

DATA_CONFIG = {
    "DEFAULT": {
        "date_col": "TIME_PERIOD",
        "country_col": "REF_AREA",
        "value_col": "OBS_VALUE"
    },
    "rpp_growth": {
        "url": "https://stats.bis.org/api/v2/data/dataflow/BIS/WS_SPP/1.0/Q.BE+CA+CH+DE+FR+GB+IT+JP+NL+SE+US.R.771?format=csv"
    },
    "credit_to_gdp_gap": {
        "url": "https://stats.bis.org/api/v2/data/dataflow/BIS/WS_CREDIT_GAP/1.0/Q.BE+CA+CH+DE+FR+GB+IT+JP+NL+SE+US.P..C?format=csv",
        "country_col": "BORROWERS_CTY"
    },
    "credit_to_gdp_ratio": {
        "url": "https://stats.bis.org/api/v2/data/dataflow/BIS/WS_CREDIT_GAP/1.0/Q.BE+CA+CH+DE+FR+GB+IT+JP+NL+SE+US.P.A.C?format=csv",
        "country_col": "BORROWERS_CTY"
    },
    "gdp_growth": {
        "url": "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAMAIN1@DF_QNA_EXPENDITURE_GROWTH_OECD,/Q..NLD+JPN+ITA+GBR+USA+FRA+SWE+DNK+CHE+CAN+BEL.S1..B1GQ......GY.?format=csvfilewithlabels",
        "country_col": "Reference area"
    },
    "central_bank_policy_rate": {
        "url": "https://stats.bis.org/api/v2/data/dataflow/BIS/WS_CBPOL/1.0/M.BE+CA+CH+DE+FR+GB+IT+JP+NL+SE+US?format=csv"
    },
    "inflation": {
        "url": "https://stats.bis.org/api/v2/data/dataflow/BIS/WS_LONG_CPI/1.0/M.BE+CA+CH+DE+FR+GB+IT+JP+NL+SE+US.771?format=csv"
    },
    "household_dti": {
        "url": "https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAAG@DF_NAAG,/A.DNK+NLD+JPN+FRA+BEL+CAN+ITA+SWE+CHE+GBR+USA.LES1M_FD4..?dimensionAtObservation=AllDimensions&format=csvfilewithlabels",
        "country_col": "Reference area"
    },
    "household_credit_to_GDP_ratio": {
        "url": "https://stats.bis.org/api/v2/data/dataflow/BIS/WS_TC/2.0/Q.BE+CA+CH+DE+FR+GB+IT+JP+NL+SE+US.H.A.M.770?format=csv",
        "country_col": "BORROWERS_CTY"
    }
}