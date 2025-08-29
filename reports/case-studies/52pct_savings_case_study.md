# Case Study: 52% Cloud Cost Reduction in 6 Months (GCP)

**Context**: Marketplace platform on GCP across GKE, GCE, BigQuery with low commitment coverage.  
**Problem**: Cost growth outpacing GMV; idle capacity; low storage hygiene.  
**Actions**:  
1. Rightsized GKE requests/limits; enabled cluster autoscaler.  
2. Schedules for non-prod; moved batch to preemptible where safe.  
3. Applied storage lifecycle + log retention controls.  
4. Purchased CUDs after stabilizing baselines; quarterly review.  
**Results**: 52% net cost reduction in six months; commitment coverage 18%→72%; storage $/GB down 35%.  
**Evidence**: Dashboard screenshots, SKU diffs, sample PRs/policies, synthetic dataset reproduction.  
**Next steps**: Unit-cost targets; anomaly alerting; predictive forecasting.  
