"""
Configurations for selected FRED data series.
"""

FRED_DATA_SERIES = {
    # S&P Dow Jones Indices LLC, S&P CoreLogic Case-Shiller U.S. National Home Price Index
    # [CSUSHPINSA], retrieved from FRED, Federal Reserve Bank of St. Louis; 
    # https://fred.stlouisfed.org/series/CSUSHPINSA, July 20, 2025.
    "cs_home_price_index": "CSUSHPINSA",

    # U.S. Bureau of Economic Analysis, Real Gross Domestic Product [GDPC1], retrieved from FRED,
    # Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/GDPC1, July 20, 2025.
    "real_gdp": "GDPC1",

    # Federal Reserve Bank of Atlanta, Sticky Price Consumer Price Index less Food and Energy
    # [CORESTICKM159SFRBATL], retrieved from FRED, Federal Reserve Bank of St. Louis; 
    # https://fred.stlouisfed.org/series/CORESTICKM159SFRBATL, July 20, 2025.
    "inflation_rate": "CORESTICKM159SFRBATL",

    # Board of Governors of the Federal Reserve System (US), Households and Nonprofit
    # Organizations; Debt Securities and Loans; Liability, Level [CMDEBT], retrieved from FRED,
    # Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CMDEBT, July 20, 2025.
    "household_debt": "CMDEBT",

    # Board of Governors of the Federal Reserve System (US), Federal Funds Effective Rate
    # [RIFSPFFNB], retrieved from FRED, Federal Reserve Bank of St. Louis; 
    # https://fred.stlouisfed.org/series/RIFSPFFNB, July 20, 2025.
    "federal_funds_rate": "RIFSPFFNB",
    
    # Board of Governors of the Federal Reserve System (US), Real Estate Loans, All Commercial
    # Banks [RELACBW027SBOG], retrieved from FRED, Federal Reserve Bank of St. Louis; 
    # https://fred.stlouisfed.org/series/RELACBW027SBOG, July 20, 2025.
    "real_estate_loans": "RELACBW027SBOG",

    # Federal Reserve Bank of St. Louis, Real M2 Money Stock [M2REAL], retrieved from FRED, Federal
    # Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/M2REAL, July 20, 2025.
    "real_m2": "M2REAL",

    # U.S. Bureau of Economic Analysis, Real Disposable Personal Income [DSPIC96], retrieved from
    # FRED, Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/DSPIC96,
    # July 20, 2025.
    "real_disposable_income": "DSPIC96",

    # U.S. Bureau of Labor Statistics, Population Level [CNP16OV], retrieved from FRED, Federal
    # Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/CNP16OV, July 20, 2025.
    "population": "CNP16OV",

    # U.S. Census Bureau and U.S. Department of Housing and Urban Development,
    # New Privately-Owned Housing Units Started: Total Units [HOUST], retrieved from FRED,
    # Federal Reserve Bank of St. Louis; https://fred.stlouisfed.org/series/HOUST,
    # July 20, 2025.
    "housing_starts": "HOUST"
}