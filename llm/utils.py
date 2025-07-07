import pandas as pd

def df_to_text(df: pd.DataFrame) -> str:
    """
    Converts a single-row DataFrame into markdown-style table text.
    """
    if df.empty:
        return "No lab data available."
    
    try:
        return df.to_markdown(index=False)
    except Exception:
        return df.to_csv(index=False)


