select * from {{ source('northwind_dbt', 'customers') }}
