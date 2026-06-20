with orders as (
    select *
    from {{ ref('stg_orders') }}
),
customers as (
    select *
    from {{ ref('stg_customers') }}
),
payments as (
    select
        order_id,
        sum(amount) as paid_amount,
        max(payment_status) as latest_payment_status
    from {{ ref('stg_payments') }}
    group by order_id
)

select
    o.order_id,
    o.customer_id,
    c.customer_name,
    c.segment,
    o.order_date,
    o.product,
    o.quantity,
    o.unit_price,
    o.gross_revenue,
    o.status as order_status,
    coalesce(p.paid_amount, 0) as paid_amount,
    coalesce(p.latest_payment_status, 'missing') as payment_status
from orders o
left join customers c
    on o.customer_id = c.customer_id
left join payments p
    on o.order_id = p.order_id