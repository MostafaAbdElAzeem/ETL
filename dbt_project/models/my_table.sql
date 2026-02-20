with data as (
    select 1 as id, 'Ahmed' as customer_name, 2 as quantity
    union all
    select 2, 'Sara', 1
    union all
    select 3, null, 5
)

select * from data