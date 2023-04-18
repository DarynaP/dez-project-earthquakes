{{ config(materialized="table") }}

select
    count(id) as n_earthquakes,
    date,
    week,
    year,
    case
        when magnitude <= 4.0
        then "green"
        when magnitude > 4.0 and magnitude <= 6.0
        then "yellow"
        else "red"
    end as alert
from {{ source("staging", "earthquake_info") }}
group by year, week, date, alert
order by date
