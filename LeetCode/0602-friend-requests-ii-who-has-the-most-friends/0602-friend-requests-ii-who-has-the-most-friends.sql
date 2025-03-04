with ids as ((select distinct requester_id as id
from RequestAccepted)
union
(select distinct accepter_id
from RequestAccepted))

select id, (select count(*) 
            from RequestAccepted
            where requester_id = i.id or accepter_id = i.id) as num
from ids i
order by num desc
limit 1