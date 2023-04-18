{{ config(materialized="table") }}

select
    id,
    date,
    country,
    longitude,
    latitude,
    magnitude,
    case
        when magnitude > 0.0 and magnitude <= 2.0
        then "Micro"
        when magnitude > 2.0 and magnitude <= 3.0
        then "Minor"
        when magnitude > 3.0 and magnitude <= 4.0
        then "Light"
        when magnitude > 4.0 and magnitude <= 5.0
        then "Moderate"
        when magnitude > 5.0 and magnitude <= 6.0
        then "Strong"
        when magnitude > 6.0 and magnitude <= 7.0
        then "Major"
        else "Great"
    end as description
from {{ source("staging", "earthquake_info") }}
