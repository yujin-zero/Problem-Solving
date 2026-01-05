with cte as (select stock_name, 
    case when operation = 'Buy' then -1 * price
        else price
    end as real_price
from Stocks)
select *
from cte