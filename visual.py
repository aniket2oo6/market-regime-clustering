import plotly.express as px

def plot_regimes(stock, ticker):
    fig = px.scatter(
        stock,
        x=stock.index,
        y="Close",
        color="Regime_Label",
        title=f"{ticker} Price Colored by Market Regime",
        labels = {"Regime_Label": "Regime"}
    )

    fig.update_layout(
        template="plotly_dark",
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    return fig
