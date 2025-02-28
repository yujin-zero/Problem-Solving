with icecream as (select *
from FIRST_HALF
union
select *
from JULY)

select FLAVOR
from icecream
group by FLAVOR
order by sum(TOTAL_ORDER) desc
limit 3