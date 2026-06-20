with base as (
    select *
    from {{ ref('int_orders_enriched') }}
)

select
    date_trunc('month', order_date) as revenue_month,
    count(*) as total_orders,
    sum(gross_revenue) as gross_revenue,
    sum(paid_amount) as paid_amount,
    sum(case when order_status = 'returned' then 1 else 0 end) as returned_orders
from base
group by 1
order by 1