with cte as (select product_id, min(year) as first_year
from Sales
group by product_id)

select c.product_id, first_year, quantity, price
from cte c 
join Sales s
on s.product_id = c.product_id and s.year = c.first_year