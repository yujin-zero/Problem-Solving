select name as Customers
from Orders o
right join Customers c
on o.customerId = c.id
where customerId is null