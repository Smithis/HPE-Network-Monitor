# Network Monitor + AI Anomaly (HPE Fullstack style) - Charan Teja
Onsite Bengaluru. UI + Python + anomaly + Docker + Jenkins stub.

## Run
```bash
pip install -r requirements.txt
pytest -q
python netmon.py
uvicorn app:app --reload  # open / for UI, /api/anomalies for JSON
```
## JD map
- UI dev: vanilla JS dashboard (fetch + render), responsive table
- Python OOP: netmon + FastAPI service
- Distributed/networking/DB/OS: synthetic metrics + anomaly correlation; note real SNMP/Prometheus next
- Docker + Jenkins: included stubs; K8s/Helm/Ansible next
- AI agents: used Copilot-style scaffolding with human review
