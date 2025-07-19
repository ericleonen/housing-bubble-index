"""
Helpers for loading data about G10 countries.
"""

import pandas as pd
from constants.g10_countries import CODE_TO_COUNTRY
from .config import DATA_CONFIG
import requests
from io import StringIO

def load_data() -> pd.DataFrame:
    default_config = DATA_CONFIG["DEFAULT"]

    df = pd.DataFrame(columns=["date", "country", "feature", "value"])

    for feature, feature_config in DATA_CONFIG.items():
        if feature == "DEFAULT":
            continue

        url = feature_config["url"]
        date_col = feature_config.get("date_col", default_config["date_col"])
        country_col = feature_config.get("country_col", default_config["country_col"])
        value_col = feature_config.get("value_col", default_config["value_col"])

        if url.startswith("https://sdmx.oecd.org"):
            feature_df = pd.read_csv(
                StringIO(requests.get(url).text)
            )
            country_values = feature_df[country_col]
        else:
            feature_df = pd.read_csv(url)
            country_values = feature_df[country_col].map(CODE_TO_COUNTRY)

        new_rows = pd.DataFrame({
            "date": feature_df[date_col],
            "country": country_values,
            "feature": feature,
            "value": feature_df[value_col]
        })

        df = pd.concat([df, new_rows], ignore_index=True)

    df["date"] = pd.to_datetime(df["date"].apply(_format_date), errors="coerce")

    df = df.pivot_table(
        index="date",
        columns=["country", "feature"],
        values="value"
    )

    return df.resample("QS") \
            .mean() \
            .interpolate(
                method="linear", 
                limit_area="inside", 
                limit_direction="both"
            ).ffill()

def _format_date(date_str):
    date_str = str(date_str).strip()

    if len(date_str) == 4:
        return pd.to_datetime(date_str + '-01-01').strftime('%Y-%m-01')
    elif 'Q' in date_str:
        return pd.Period(date_str, freq='Q').start_time.strftime('%Y-%m-01')
    else:
        return pd.to_datetime(date_str).strftime('%Y-%m-01')