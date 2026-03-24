with cte as (select book_id, count(*) as cnt
from borrowing_records
where return_date is null
group by book_id)

select *
from library_books lb
join cte c
on lb.book_id = c.book_id
where total_copies = cnt