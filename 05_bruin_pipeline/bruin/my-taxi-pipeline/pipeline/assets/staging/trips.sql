/* @bruin
name: staging.trips
type: bq.sql
connection: google_cloud_platform
depends:
  - ingestion.trips
  - ingestion.payment_lookup
materialization:
  type: table
  strategy: create+replace
columns:
  - name: trip_distance
    checks:
      - name: non_negative
  - name: total_amount
    checks:
      - name: non_negative
@bruin */
SELECT 
    VendorID AS vendor_id,
    tpep_pickup_datetime AS pickup_datetime,
    tpep_dropoff_datetime AS dropoff_datetime,
    passenger_count,
    trip_distance,
    RatecodeID AS rate_code_id,
    payment_type,
    total_amount
FROM 
    `ingestion.trips`
WHERE 
    total_amount >= 0 
    AND trip_distance >= 0