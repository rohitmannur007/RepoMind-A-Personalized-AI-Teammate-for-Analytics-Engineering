select
    payment_id,
    order_id,
    cast(payment_date as date) as payment_date,
    cast(amount as double) as amount,
    payment_method,
    payment_status
from {{ ref('payments') }}