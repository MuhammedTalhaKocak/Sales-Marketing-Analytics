import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def plot_segment_distribution(rfm: pd.DataFrame) -> go.Figure:
    segment_counts = rfm["Segment"].value_counts().reset_index()
    segment_counts.columns = ["Segment", "Count"]
    fig = px.bar(segment_counts, x="Segment", y="Count", title="Segment Counts")
    return fig


def plot_avg_monterary_per_segments(rfm: pd.DataFrame) -> go.Figure:
    avg_monetary_per_segments = (
        rfm.groupby("Segment").agg({"Monetary": "mean"}).reset_index()
    )
    fig = px.bar(
        avg_monetary_per_segments,
        x="Segment",
        y="Monetary",
        title="Müşteri Segment Dağılımı",
        labels={"Segment": "Segment", "Count": "Müşteri Sayısı"},
        color="Segment",
    )
    return fig


def plot_scatter(rfm: pd.DataFrame) -> go.Figure:
    scatter = px.scatter(
        rfm,
        x="Recency",
        y="Monetary",
        color="Segment",
        title="Recency vs Monetary — Segment Bazında",
        labels={"Recency": "Recency (Gün)", "Monetary": "Toplam Harcama (£)"},
    )
    return scatter
