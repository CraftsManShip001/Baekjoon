select book_id,to_char(published_date,'YYYY-MM-DD') as published_date
from book
where category = '인문' and to_char(published_date,'YYYY') = '2021'
order by published_date