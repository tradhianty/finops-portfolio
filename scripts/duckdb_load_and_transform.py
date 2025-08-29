import duckdb
import os
con = duckdb.connect(database=':memory:')
con.execute("""CREATE TABLE aws AS SELECT * FROM read_csv_auto('data/synthetic/aws_cur_sample.csv');""")
con.execute("""CREATE TABLE mapping AS SELECT * FROM read_csv_auto('data/synthetic/org_mapping.csv');""")
# normalize column names and compute monthly totals
con.execute('''
CREATE TABLE monthly AS
SELECT
  date_trunc('month', CAST(line_item_usage_start_date AS DATE))::DATE AS invoice_month,
  tags_team AS team,
  SUM(line_item_net_cost) AS month_cost
FROM aws
GROUP BY 1,2;
''')
# allocate
con.execute('''
CREATE TABLE allocated AS
SELECT m.invoice_month, mp.subsidiary, m.team, m.month_cost * mp.allocation_weight AS allocated_cost
FROM monthly m JOIN mapping mp ON mp.team = m.team
ORDER BY 1,2;
''')
con.execute("COPY allocated TO 'outputs/allocated_costs.csv' (HEADER TRUE);")
print('Allocated results written to outputs/allocated_costs.csv')
