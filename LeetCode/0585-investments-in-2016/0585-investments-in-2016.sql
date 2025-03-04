with cte as (select tiv_2015
from Insurance
group by tiv_2015
having count(*) > 1),
cte2 as (
select *
from Insurance
group by lat, lon
having count(*) = 1 and tiv_2015 in (select * from cte))

select round(sum(tiv_2016),2) as tiv_2016
from cte2