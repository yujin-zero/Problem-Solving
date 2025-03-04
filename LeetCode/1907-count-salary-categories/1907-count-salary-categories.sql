with cate as(
select 'Low Salary' as category
union select 'Average Salary'
union select 'High Salary'),
cte as(
select account_id, income, 
case when income < 20000 then 'Low Salary'
     when income <= 50000 then 'Average Salary'
     else 'High Salary'
end as category
from Accounts)

select category, (
    select count(*) 
    from cte
    where category = c.category
    ) as accounts_count
from cate c