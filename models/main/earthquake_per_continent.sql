{{ config(materialized="table") }}

select
    count(id) as n_earthquakes,
    year,
    week,
    {{ dbt_date.month_name(date, short=false) }} as month,
    continent
from {{ source("staging", "earthquake_info") }}
group by year, week, month, continent
order by week
