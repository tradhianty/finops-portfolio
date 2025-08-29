# Multi-Cloud Price Comparison (Dummy Data)  

**Scenario:**  
Analyzed workload costs across **AWS vs GCP** using dummy workloads.  

**Workload Profile (Dummy):**  
- 500 VM hours  
- 5 TB Storage  
- 10 TB Data Transfer  

**Results:**  
| Cloud | Cost ($) | Notes |
|-------|----------|-------|
| AWS   | 6,200    | Higher data transfer costs |
| GCP   | 5,500    | Cheaper sustained-use discounts |

**Visualization:**  

![Dummy Cost Comparison](https://quickchart.io/chart?c={type:'bar',data:{labels:['AWS','GCP'],datasets:[{label:'Monthly Cost ($)',data:[6200,5500]}]}})
