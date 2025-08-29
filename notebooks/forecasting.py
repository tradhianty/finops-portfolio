# Forecasting (monthly) – skeleton
import pandas as pd
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt

df = pd.read_csv('../data/synthetic/gcp_billing_sample.csv', parse_dates=['usage_start_time'])
monthly = df.groupby(pd.Grouper(key='usage_start_time', freq='MS'))['net_cost'].sum()

model = SARIMAX(monthly, order=(1,1,1), seasonal_order=(0,1,1,12), enforce_stationarity=False, enforce_invertibility=False)
res = model.fit(disp=False)
fc = res.get_forecast(steps=3)
pred = fc.predicted_mean
ci = fc.conf_int()

ax = monthly.plot(figsize=(8,4), label='observed')
pred.plot(ax=ax, label='forecast')
ax.fill_between(ci.index, ci.iloc[:,0], ci.iloc[:,1], alpha=0.2)
ax.set_title('Monthly Net Cost Forecast')
ax.legend()
plt.tight_layout()
plt.savefig('forecast.png')
print('Saved forecast.png')