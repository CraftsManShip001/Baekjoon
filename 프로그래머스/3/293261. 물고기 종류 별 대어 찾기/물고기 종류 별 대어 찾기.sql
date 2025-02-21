select a.id,b.fish_name,a.length
from fish_info as a,fish_name_info as b
where a.fish_type = b.fish_type and
a.length = (
    select max(length)
    from fish_info
    where fish_type = a.fish_type
)
order by a.id