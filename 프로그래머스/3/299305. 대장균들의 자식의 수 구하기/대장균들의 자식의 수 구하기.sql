select id, ifnull(
    (
    select 
        count(*) 
        from ecoli_data 
        group by parent_id
        having parent_id = id
),0)as child_count
from ecoli_data
order by id