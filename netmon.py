import numpy as np, pandas as pd
from sklearn.ensemble import IsolationForest
def make_metrics(n=800, seed=11):
    rng = np.random.default_rng(seed)
    latency = rng.normal(45, 8, n)
    loss = np.abs(rng.normal(0.4, 0.3, n))
    idx = rng.choice(n, 15, replace=False)
    latency[idx] = rng.normal(180, 30, 15)
    loss[idx] = rng.normal(5.0, 1.5, 15)
    return pd.DataFrame({"latency_ms": latency, "loss_pct": loss}), set(idx)
def detect(df):
    clf = IsolationForest(contamination=0.02, random_state=11)
    pred = clf.fit_predict(df[["latency_ms","loss_pct"]].values)
    return pred, -clf.score_samples(df[["latency_ms","loss_pct"]].values)
if __name__ == "__main__":
    df, true_idx = make_metrics()
    pred, _ = detect(df)
    import numpy as np
    flagged = set(np.where(pred==-1)[0])
    print(f"flagged={len(flagged)} recall={len(flagged & true_idx)/len(true_idx):.2f}")
