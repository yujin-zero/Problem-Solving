select firstName, lastName, city, state
from Address a
right join Person p
on a.personId = p.personId