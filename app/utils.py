import pandas as pd


def format_error(message: str) -> dict[str, str]:
    return {"error": message}


def normalize_columns(dataframe: pd.DataFrame) -> pd.DataFrame:
    if isinstance(dataframe.columns, pd.MultiIndex):
        dataframe.columns = dataframe.columns.get_level_values(0)
    return dataframe
