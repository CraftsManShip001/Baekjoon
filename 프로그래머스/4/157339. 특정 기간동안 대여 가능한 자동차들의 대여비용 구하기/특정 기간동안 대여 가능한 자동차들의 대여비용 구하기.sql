select a.car_id,a.car_type,round(((a.daily_fee - (a.daily_fee * (c.discount_rate / 100))) * 30),0) as fee
from CAR_RENTAL_COMPANY_CAR as a,
    CAR_RENTAL_COMPANY_RENTAL_HISTORY as b,
    CAR_RENTAL_COMPANY_DISCOUNT_PLAN as c
where a.car_id = b.car_id and a.car_type = c.car_type and
a.CAR_ID NOT IN (
    SELECT CAR_ID
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE END_DATE > '2022-11-01' AND START_DATE < '2022-12-01'
) and
c.duration_type = '30일 이상'and
(a.car_type = '세단' or a.car_type = 'SUV') and
((a.daily_fee - (a.daily_fee * (c.discount_rate / 100))) * 30) between 500000 and 2000000
GROUP BY a.CAR_ID
order by ((a.daily_fee - (a.daily_fee * (c.discount_rate / 100))) * 30) desc,
a.car_type, a.car_id desc