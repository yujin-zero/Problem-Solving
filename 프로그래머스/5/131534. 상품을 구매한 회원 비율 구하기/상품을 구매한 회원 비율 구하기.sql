with cte as (select count(*) from USER_INFO where year(joined) = 2021)

select year(sales_date) as YEAR, month(sales_date) as MONTH, count(distinct s.user_id) as PURCHASED_USERS,
    round(count(distinct s.user_id)/(select * from cte),1) as PUCHASED_RATIO
from ONLINE_SALE s
join USER_INFO i on s.USER_ID = i.USER_ID
where year(JOINED) = 2021
group by year(sales_date), month(sales_date)
order by YEAR, MONTH