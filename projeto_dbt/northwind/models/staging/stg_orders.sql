select * from {{ source('northwind_dbt', 'orders') }}
