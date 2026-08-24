from flask import Flask, render_template, request
from data import load_data
from clustering import fit_gmm, label
from visual import plot_regimes

app = Flask(__name__)

@app.route("/", methods = ["POST", "GET"])
def index():
    chart = None
    if request.method == "POST":
        ticker = request.form["ticker"]
        stock = load_data(ticker)

        if stock.empty:
            return render_template("index.html", error = f"No data found for '{ticker}'", ticker = ticker)

        stock, gmm = fit_gmm(stock)
        stock = label(stock)

        regime_label_map = dict(zip(stock["Regime"], stock["Regime_Label"]))

        latest = stock.iloc[-1]
        regime_prob = {
            regime_label_map[i]: round(latest[f"Prob_Regime_{i}"] * 100, 1)
            for i in regime_label_map
        }

        fig = plot_regimes(stock, ticker)
        chart = fig.to_html(full_html = False)

        return render_template("index.html", chart = chart, ticker = ticker, regime_prob = regime_prob)

    return render_template("index.html", chart = chart)

if __name__ == "__main__":
    app.run(debug = True)

