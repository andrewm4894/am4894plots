import pandas as pd
import re


def get_cols_like(df: pd.DataFrame, cols_like: list) -> list:
    df_columns = df.columns
    cols_like = [like.replace('%', '.*') for like in cols_like]
    cols = []
    for like in cols_like:
        pattern = re.compile(f'^{like}$')
        matched_cols = [col for col in df_columns if pattern.match(col)]
        cols.extend(matched_cols)
    cols = list(set(cols))
    return cols
