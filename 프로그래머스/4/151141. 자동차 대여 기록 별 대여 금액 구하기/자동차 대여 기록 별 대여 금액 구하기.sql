with history as (select history_id, datediff(end_date,start_date)+1 as dd, daily_fee,
case when datediff(end_date,start_date)+1 >= 90 then '90일 이상'
     when datediff(end_date,start_date)+1 >= 30 then '30일 이상'
     when datediff(end_date,start_date)+1 >= 7 then '7일 이상'
end as DURATION_TYPE
from CAR_RENTAL_COMPANY_RENTAL_HISTORY h
join CAR_RENTAL_COMPANY_CAR c on h.car_id = c.car_id
where car_type = '트럭')

select HISTORY_ID, round(daily_fee * dd * (100-ifnull(discount_rate,0))/100) as FEE
from history h
left join CAR_RENTAL_COMPANY_DISCOUNT_PLAN p 
on h.DURATION_TYPE = p.DURATION_TYPE and CAR_TYPE = '트럭'
order by FEE desc, HISTORY_ID desc