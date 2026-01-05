with cte as (select stock_name, 
    case when operation = 'Buy' then -1 * price
        else price
    end as real_price
from Stocks)
select stock_name, sum(real_price) as capital_gain_loss
from cte
group by stock_name