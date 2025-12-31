with cte as (select p.product_id, units, (units * price) as up
from UnitsSold u
left join Prices p
on u.product_id = p.product_id and purchase_date >= start_date and 
    purchase_date <= end_date),
cte2 as (select product_id, round((sum(up)/sum(units)),2) as average_price
from cte
group by product_id)
select p.product_id, ifnull(average_price,0) as 'average_price'
from Prices p
left join cte2 c
on p.product_id = c.product_id
group by product_id