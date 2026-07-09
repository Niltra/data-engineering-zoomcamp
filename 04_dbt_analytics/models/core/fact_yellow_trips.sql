{{ config(materialized='table') }}

select
    vendor_id,
    pickup_datetime,
    dropoff_datetime,
    passenger_count,
    trip_distance,
    total_amount
from {{ ref('stg_yellow_tripdata') }}
where passenger_count > 0 
  and trip_distance > 0