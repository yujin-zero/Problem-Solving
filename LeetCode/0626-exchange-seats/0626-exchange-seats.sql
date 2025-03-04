select a.id, ifnull(b.student,a.student) as student
from Seat a 
left join Seat b on
case when a.id % 2 = 0 then a.id = b.id+1
     else a.id = b.id-1
end
order by a.id