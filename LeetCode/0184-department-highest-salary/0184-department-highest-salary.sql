-- select departmentId, max(salary) as ms
-- from Employee
-- group by departmentId

select d.name as 'Department', e.name as 'Employee', salary as 'Salary'
from Employee e
join Department d
on e.departmentId = d.id
where (departmentId, salary) in (
    select departmentId, max(salary) as ms
    from Employee
    group by departmentId)