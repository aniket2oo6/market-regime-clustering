from sklearn.preprocessing import StandardScaler
from sklearn.mixture import GaussianMixture

def  fit_gmm(stock, n_components = 3):
    features = stock[["Return", "Volatility"]]
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    gmm = GaussianMixture(n_components = n_components, random_state = 10)
    gmm.fit(scaled_features)

    labels = gmm.predict(scaled_features)
    prob = gmm.predict_proba(scaled_features)

    stock["Regime"] = labels

    for i in range(prob.shape[1]):
        stock[f"Prob_Regime_{i}"] = prob[:, i]

    return stock, gmm

def label(spy):
    stats = spy.groupby("Regime")["Volatility"].mean()
    sorted_stats = stats.sort_values().index.tolist()

    labels = ["Calm", "Elevated", "Crisis"]
    labels_map = dict(zip(sorted_stats, labels))

    spy["Regime_Label"] = spy["Regime"].map(labels_map)
    return spy
