import pandas as pd


def reference_date(df: pd.DataFrame) -> pd.DataFrame:
    reference_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)
    return reference_date


def calculate_rfm(df: pd.DataFrame, reference_date: pd.Timestamp) -> pd.DataFrame:
    rfm = (
        df.groupby("Customer ID")
        .agg(
            Recency=("InvoiceDate", lambda x: (reference_date - x.max()).days),
            Frequency=("Invoice", "nunique"),
            Monetary=("Revenue", "sum"),
        )
        .reset_index()
    )
    rfm["Customer ID"] = rfm["Customer ID"].astype(int)
    return rfm


def rfm_score(df: pd.DataFrame) -> pd.DataFrame:
    df["R_Score"] = pd.qcut(df["Recency"], q=4, labels=[4, 3, 2, 1])
    df["F_Score"] = pd.qcut(
        df["Frequency"].rank(method="first"), q=4, labels=[1, 2, 3, 4]
    )
    df["M_Score"] = pd.qcut(
        df["Monetary"].rank(method="first"), q=4, labels=[1, 2, 3, 4]
    )
    df["RFM_Score"] = (
        df["R_Score"].astype(int)
        + df["F_Score"].astype(int)
        + df["M_Score"].astype(int)
    )
    return df


def segment(df: pd.DataFrame) -> pd.DataFrame:
    df["Segment"] = pd.cut(
        df["RFM_Score"],
        bins=[0, 3, 6, 9, 12],
        labels=[
            "Kayıp Müşteriler",
            "Risk Altındakiler",
            "Sadık Müşteriler",
            "Şampiyonlar",
        ],
    )
    return df
