with cte as (select mr.movie_id, mr.user_id, rating, created_at, name, title
from MovieRating mr
join Users u on u.user_id = mr.user_id
join Movies m on m.movie_id = mr.movie_id)

(select name as results
from cte
group by user_id
order by count(*) desc, name
limit 1)
union all
(select title
from cte
where created_at between '2020-02-01' and '2020-02-29'
group by movie_id
order by avg(rating) desc, title
limit 1)