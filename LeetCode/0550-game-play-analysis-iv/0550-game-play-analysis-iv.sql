with cte as (select player_id, min(event_date) + interval 1 day as find_day
from Activity
group by player_id)

select round(sum(case
when find_day in (
    select event_date from Activity where player_id = c.player_id) then 1
else 0
end) / count(*),2) as fraction
from cte c