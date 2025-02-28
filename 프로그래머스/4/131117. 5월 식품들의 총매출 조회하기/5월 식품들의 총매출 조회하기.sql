SELECT o.PRODUCT_ID, PRODUCT_NAME, sum(price*amount) as TOTAL_SALES
from FOOD_ORDER o
join FOOD_PRODUCT p
on o.PRODUCT_ID = p.PRODUCT_ID
where year(PRODUCE_DATE) = 2022 and month(PRODUCE_DATE) = 5
group by o.PRODUCT_ID
order by TOTAL_SALES desc, o.PRODUCT_ID