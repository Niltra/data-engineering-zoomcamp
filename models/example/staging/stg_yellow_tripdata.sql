{{ config(materialized='view') }}

select
    -- Identificadores
    cast(vendorid as integer) as vendor_id,

    -- Fechas y horas (Renombramos para que sea más legible)
    cast(tpep_pickup_datetime as timestamp) as pickup_datetime,
    cast(tpep_dropoff_datetime as timestamp) as dropoff_datetime,

    -- Información del viaje
    cast(passenger_count as integer) as passenger_count,
    cast(trip_distance as numeric) as trip_distance,

    -- Información de pago
    cast(total_amount as numeric) as total_amount

from {{ source('staging', 'yellow_tripdata_partitioned_clustered') }}