with recursive ECOLI as (
    select id, parent_id, 1 as GENERATION
    from ECOLI_DATA
    where parent_id is null
    
    union all
    
    select d.id, d.parent_id, e.GENERATION+1
    from ECOLI e
    join ECOLI_DATA d on e.id = d.parent_id
)

select count(*) as COUNT, GENERATION
from ECOLI
where id not in (select distinct parent_id from ECOLI_DATA where parent_id is not null)
group by GENERATION
