/* @bruin
name: reports.trips_report
type: bq.sql
connection: google_cloud_platform
depends:
  - staging.trips
materialization:
  type: table
  strategy: create+replace
@bruin */

SELECT 
    payment_type,
    COUNT(vendor_id) AS total_trips,
    AVG(trip_distance) AS avg_trip_distance,
    SUM(total_amount) AS total_revenue
FROM 
    `staging.trips`
GROUP BY 
    payment_type
ORDER BY 
    total_revenue DESC;