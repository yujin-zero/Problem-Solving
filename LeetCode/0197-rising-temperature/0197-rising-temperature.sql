select w2.id
from weather w
join weather w2
on date(w.recordDate) + interval 1 day = date(w2.recordDate)
where w.temperature < w2.temperature