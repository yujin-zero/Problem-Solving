with dday as (select distinct visited_on
from Customer
where visited_on > (select min(visited_on) from Customer) + interval 5 day),
cte as(
select visited_on, 
        (select sum(amount)
        from Customer
        where visited_on between d.visited_on - interval 6 day and d.visited_on
    ) as amount
from dday d)

select visited_on, amount, round(amount/7,2) as average_amount
from cte