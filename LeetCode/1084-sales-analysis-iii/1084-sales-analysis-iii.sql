select distinct s.product_id, product_name
from Sales s
join Product p
on s.product_id = p.product_id
where sale_date >= '2019-01-01' && sale_date <= '2019-03-31' && s.product_id not in 
    (select product_id
    from Sales
    where sale_date < '2019-01-01' || sale_date > '2019-03-31')