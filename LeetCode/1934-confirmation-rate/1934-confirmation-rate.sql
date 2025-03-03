with cte as (
    select user_id, count(*) as total, sum(action = 'confirmed') as confirm
    from Confirmations
    group by user_id)

select user_id, ifnull(round((select confirm from cte where user_id = s.user_id) / (select total from cte where user_id = s.user_id),2),0.00) as confirmation_rate
from Signups s