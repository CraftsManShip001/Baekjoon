select rest_review.rest_id, rest_name,food_type,favorites,address,round(avg(rest_review.review_score),2) as SCORE
from rest_review,rest_info
where rest_review.rest_id = rest_info.rest_id and address like '서울%'
group by rest_review.rest_id, rest_name,food_type,favorites,address
order by round(avg(rest_review.review_score),2) desc, favorites desc