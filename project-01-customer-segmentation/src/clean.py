import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_excel(path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df["Description"] = df["Description"].fillna(value="Unknown")
    df = df.dropna(subset=["Customer ID"])
    df.loc[:, "Customer ID"] = df["Customer ID"].astype(int)
    df = df[~df["Invoice"].astype(str).str.startswith("C")]
    df = df[df["Quantity"] > 0]
    df = df[df["Price"] > 0]
    df = df.drop_duplicates()
    return df


def add_revenue(df: pd.DataFrame) -> pd.DataFrame:
    df["Revenue"] = df["Quantity"] * df["Price"]
    return df
