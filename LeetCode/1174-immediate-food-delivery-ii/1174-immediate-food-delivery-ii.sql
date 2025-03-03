with cte as (select customer_id, min(order_date) as od
from Delivery
group by customer_id),
cte2 as (
    select od, (select customer_pref_delivery_date from Delivery
    where customer_id = c.customer_id and order_date = c.od) as cpdd
    from cte c
)
select round(sum(od = cpdd) / count(*) * 100,2) as immediate_percentage
from cte2
