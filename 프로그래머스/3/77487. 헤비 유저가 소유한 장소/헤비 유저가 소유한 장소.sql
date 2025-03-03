select *
from places
where host_id in (select HOST_ID
from places
group by HOST_ID
having count(*) >= 2)