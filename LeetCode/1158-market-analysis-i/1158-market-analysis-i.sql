with cte as (select buyer_id, count(*) as cnt
from Orders
where year(order_date) = 2019
group by buyer_id)
select user_id as buyer_id, join_date, ifnull(cnt, 0) as orders_in_2019
from Users u
left join cte c
on u.user_id = c.buyer_id