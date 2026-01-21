select name, sum(amount) as balance
from Transactions t
join Users u
on t.account = u.account
group by name
having sum(amount) > 10000