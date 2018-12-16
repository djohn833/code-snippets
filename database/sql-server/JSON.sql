-- Add a new field to the front of a JSON object.
SELECT jsonString.value, newJsonString.value
FROM (VALUES ('{}'), ('{"foo":13}')) jsonString(value)
CROSS APPLY (SELECT CASE WHEN LEN(jsonString.value) > 2 THEN ',' ELSE '' END) commaIfNeeded(value)
CROSS APPLY (SELECT '{"bar":42' + commaIfNeeded.value + STUFF(jsonString.Value, 1, 1, '')) newJsonString(value)


/*

SELECT compatibility_level FROM sys.databases WHERE name = 'DatabaseName';

-- Compatibility level must be 130 or higher.
ALTER DATABASE [DatabaseName] SET COMPATIBILITY_LEVEL = 130;

-- Set compatibility level back.
ALTER DATABASE [DatabaseName] SET COMPATIBILITY_LEVEL = 110;

*/

DECLARE @json nvarchar(max) = N'{"Name":{"first":"Siegward","middle":"Liesbeth","last":"Beyersdorf"}}';

SELECT
	json.*
FROM OPENJSON(@json)
	WITH
	(
		 LastName   nvarchar(50) '$.Name.last'
		,FirstName  nvarchar(50) '$.Name.first'
		,MiddleName nvarchar(50) '$.Name.middle'
	) json


SELECT
	jsonString.value
FROM OPENJSON(@json)
	WITH
	(
		 LastName   nvarchar(50) '$.Name.last'
		,FirstName  nvarchar(50) '$.Name.first'
		,MiddleName nvarchar(50) '$.Name.middle'
	) json
CROSS APPLY
	(
		SELECT
			 json.LastName   as 'Name.last'
			,json.FirstName  as 'Name.first'
			,json.MiddleName as 'Name.middle'
		FOR JSON PATH, WITHOUT_ARRAY_WRAPPER
	) jsonString(value)
