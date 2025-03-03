with milk as (select cart_id from CART_PRODUCTS where name = 'Milk'),
yogurt as (
    select cart_id 
    from CART_PRODUCTS 
    where name = 'Yogurt')

select distinct CART_ID
from CART_PRODUCTS
where CART_ID in (select * from milk) and CART_ID in (select * from yogurt)