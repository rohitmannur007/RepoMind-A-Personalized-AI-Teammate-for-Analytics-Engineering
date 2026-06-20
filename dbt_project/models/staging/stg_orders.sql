select
    order_id,
    customer_id,
    cast(order_date as date) as order_date,
    product,
    cast(quantity as integer) as quantity,
    cast(unit_price as double) as unit_price,
    status,
    cast(quantity as double) * cast(unit_price as double) as gross_revenue
from {{ ref('orders') }}