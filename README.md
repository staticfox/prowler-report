# prowler-report
Quick prototype for rendering Prowler scan CSV exports in pretty HTML

## Setup

```
git clone https://github.com/lalanza808/prowler-report
cd prowler-report
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Running

I've hardcoded paths for now. Make sure your CSV export is stored in this directory as "prowler-test.csv"

```
.venv/bin/python generate_report.py
```
