with cte as (select e.id, e.name as Employee, salary, d.name as Department, dense_rank() over (partition by departmentId order by salary desc) as r
from Employee e
join Department d on e.departmentId = d.id)

select Department, Employee, salary
from cte
where r <= 3
