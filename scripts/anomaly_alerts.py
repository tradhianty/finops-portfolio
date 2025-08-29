import pandas as pd
import sys

df = pd.read_csv("data/synthetic/gcp_billing_sample.csv", parse_dates=["usage_start_time"])
daily = df.groupby(["usage_start_time","labels.team"])["net_cost"].sum().reset_index()
daily = daily.sort_values(["labels.team","usage_start_time"])
daily["prev_cost"] = daily.groupby("labels.team")["net_cost"].shift(1)
daily["pct_change"] = (daily["net_cost"] - daily["prev_cost"]) / daily["prev_cost"] * 100
alerts = daily[(daily["prev_cost"]>0) & (daily["pct_change"].abs() >= 30)]

if alerts.empty:
    print("No anomalies over ±30% found.")
else:
    print("Anomalies (±30% DoD):")
    for _, r in alerts.iterrows():
        print(f"{r['usage_start_time'].date()} | {r['labels.team']:<12} | ${r['prev_cost']:.2f} -> ${r['net_cost']:.2f} ({r['pct_change']:.1f}%)")
