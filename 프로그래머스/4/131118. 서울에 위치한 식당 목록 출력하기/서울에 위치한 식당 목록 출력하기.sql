# select rest_info.rest_id, rest_name,food_type,favorites,address,round(avg(review_score),2) as score
# from rest_info,rest_review
# where address like '서울%'
# group by rest_info.rest_id
# order by avg(review_score) desc, favorites desc

select rest_review.rest_id, rest_name,food_type,favorites,address,round(avg(rest_review.review_score),2) as SCORE
from rest_review,rest_info
where rest_review.rest_id = rest_info.rest_id and address like '서울%'
group by rest_review.rest_id
order by round(avg(rest_review.review_score),2) desc, favorites desc