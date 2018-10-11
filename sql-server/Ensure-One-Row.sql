-- Ensure at least one row
SELECT EnsureAtLeastOneRow.*
FROM (SELECT 1) OneRow(Value)
OUTER APPLY
(
    -- Put original query here
) EnsureAtLeastOneRow

-- Ensure exactly one row
SELECT TOP 1 EnsureExactlyOneRow.*
FROM (SELECT 1) OneRow(Value)
OUTER APPLY
(
    -- Put original query here
) EnsureExactlyOneRow

