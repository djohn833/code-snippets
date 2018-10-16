SELECT jsonString.value, newJsonString.value
FROM (VALUES ('{}'), ('{"foo":13}')) jsonString(value)
CROSS APPLY (SELECT SUBSTRING(jsonString.value, 1, LEN(jsonString.value) - 1) + CASE WHEN LEN(jsonString.value) > 2 THEN ',' ELSE '' END + '"bar":42}') newJsonString(value)
