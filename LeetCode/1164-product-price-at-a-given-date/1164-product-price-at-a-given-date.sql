with cte as(select product_id, max(change_date) as cd
from Products
where change_date <= '2019-08-16'
group by product_id),
cte2 as (
select c.product_id, new_price
from cte c 
join Products p on p.product_id = c.product_id and p.change_date = c.cd),
product as (select distinct product_id from Products)

select product_id, ifnull((select new_price from cte2 where product_id = p.product_id),10) as price
from product p