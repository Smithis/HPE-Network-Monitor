from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from netmon import make_metrics, detect
import numpy as np
app = FastAPI(title="HPE-style Network Monitor - Charan Teja")
@app.get("/", response_class=HTMLResponse)
def ui():
    return """<html><head><title>Net Monitor</title>
<style>body{font-family:Arial;margin:24px}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:6px}.bad{background:#ffd6d6}</style></head>
<body><h3>Network Performance - anomaly demo</h3>
<p>Backend: FastAPI + IsolationForest. UI: vanilla JS fetch. Docker + Jenkins stub included.</p>
<button onclick="load()">Load anomalies</button><div id="out"></div>
<script>async function load(){const r=await fetch('/api/anomalies');const j=await r.json();
document.getElementById('out').innerHTML='flagged='+j.flagged+' recall='+j.recall+'<br>'+j.rows.map(x=>`<div class=${x.anomaly?'bad':''}>${x.latency_ms.toFixed(1)}ms loss ${x.loss_pct.toFixed(2)}% ${x.anomaly?'ANOMALY':''}</div>`).join('')}</script>
</body></html>"""
@app.get("/api/anomalies")
def api():
    df, true_idx = make_metrics()
    pred, _ = detect(df)
    flagged = set(np.where(pred==-1)[0])
    rows = [{"latency_ms": float(df.iloc[i].latency_ms), "loss_pct": float(df.iloc[i].loss_pct), "anomaly": bool(pred[i]==-1)} for i in range(min(50, len(df)))]
    return {"flagged": len(flagged), "recall": round(len(flagged & true_idx)/len(true_idx), 2), "rows": rows}
