-- Allocate costs from billing to subsidiaries using org_mapping
-- Assumes billing table has 'tags_team' and 'line_item_net_cost'
WITH billing AS (
  SELECT
    line_item_usage_start_date::DATE AS usage_date,
    product_product_name AS service,
    tags_team AS team,
    line_item_net_cost AS net_cost
  FROM read_csv_auto('data/synthetic/aws_cur_sample.csv')
),
mapping AS (
  SELECT * FROM read_csv_auto('data/synthetic/org_mapping.csv')
),
monthly AS (
  SELECT date_trunc('month', usage_date)::date AS invoice_month, team, SUM(net_cost) AS month_cost
  FROM billing
  GROUP BY 1,2
),
alloc AS (
  SELECT m.invoice_month,
         mp.subsidiary,
         m.team,
         m.month_cost * mp.allocation_weight AS allocated_cost
  FROM monthly m
  JOIN mapping mp ON mp.team = m.team
)
SELECT * FROM alloc ORDER BY invoice_month, subsidiary;
