select EnsureAtLeastOneRow.*
from (select 1)
left join
(
    -- Put original query here
) EnsureAtLeastOneRow on 1 = 1;

select EnsureExactlyOneRow.*
from (select 1)
left join
(
    -- Put original query here
) EnsureExactlyOneRow on 1 = 1
limit 1;

