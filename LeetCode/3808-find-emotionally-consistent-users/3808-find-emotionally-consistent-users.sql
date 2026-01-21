with cte as (
    select user_id ,count(*) as cnt
    from reactions
    group by user_id
    having count(*) >= 5), 
cte2 as (
select r.user_id, reaction, round(count(*)/cnt,2) as reaction_ratio
from reactions r 
join cte c 
on r.user_id = c.user_id
group by user_id, reaction)

select user_id, reaction as dominant_reaction, reaction_ratio
from cte2
where reaction_ratio >= 0.6
order by reaction_ratio desc