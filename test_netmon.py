from netmon import make_metrics, detect
import numpy as np
def test_recall():
    df, true_idx = make_metrics()
    pred, _ = detect(df)
    flagged = set(np.where(pred==-1)[0])
    assert len(flagged & true_idx)/len(true_idx) >= 0.6
def test_api():
    from fastapi.testclient import TestClient
    from app import app
    c = TestClient(app)
    assert c.get("/").status_code == 200
    j = c.get("/api/anomalies").json()
    assert "flagged" in j and "rows" in j
