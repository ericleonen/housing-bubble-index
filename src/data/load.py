"""
Helper for preprocessing and loading U.S. macroeconomic data from FRED.
"""

import pandas as pd
from data.config import FRED_DATA_SERIES
import fredapi
import dotenv
import os

def load_data() -> pd.DataFrame:
    dotenv.load_dotenv()
    FRED_API_KEY = os.getenv("FRED_API_KEY")
    fred = fredapi.Fred(api_key=FRED_API_KEY)

    data = pd.DataFrame({
        name: fred.get_series(
            series_id=code
        ).resample("MS").mean().interpolate(
            limit_area="inside", 
            limit_direction="forward"
        ).ffill()
        for name, code in FRED_DATA_SERIES.items()
    }).dropna()

    # Endogenous variable
    data["cs_home_price_growth"] = data["cs_home_price_index"].pct_change(periods=12) * 100

    # Exogeneous variables: general macroeconomic conditions
    data["real_gdp_growth"] = data["real_gdp"].pct_change(periods=12) * 100
    # data["inflation_rate"]
    # data["federal_funds_rate"]

    # # Exogeneous variables: housing market conditions
    data["real_disposable_income_growth"] = data["real_disposable_income"].pct_change(periods=12) * 100
    data["housing_starts_growth"] = data["housing_starts"].pct_change(periods=12) * 100
    data["population_growth"] = data["population"].pct_change(periods=12) * 100

    # Exogeneous variables: credit-exuberance
    data["household_debt_growth"] = data["household_debt"].pct_change(periods=12) * 100
    data["real_estate_loans_growth"] = data["real_estate_loans"].pct_change(periods=12) * 100
    data["real_m2_growth"] = data["real_m2"].pct_change(periods=12) * 100

    data = data.drop(
        columns=[
            "cs_home_price_index",
            "real_gdp",
            "real_disposable_income",
            "housing_starts",
            "population",
            "household_debt",
            "real_estate_loans",
            "real_m2"
        ]
    ).dropna()

    return data