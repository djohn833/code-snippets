SELECT EnsureAtLeastOneRow.*
FROM (SELECT 1)
LEFT JOIN
(
    -- Put original query here
) EnsureAtLeastOneRow ON 1 = 1;

SELECT EnsureExactlyOneRow.*
FROM (SELECT 1)
LEFT JOIN
(
    -- Put original query here
) EnsureExactlyOneRow ON 1 = 1
LIMIT 1;

