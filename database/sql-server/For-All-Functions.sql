SET NOCOUNT ON;

DECLARE @function_full_name NVARCHAR(MAX);

DECLARE function_cursor CURSOR FOR
	SELECT N'[' + SCHEMA_NAME(o.schema_id) + N'].[' + o.name + N']'
	FROM sys.objects o
	WHERE 0 = 1
	   OR o.type = 'IF' -- Inline function
	   OR o.type = 'TF' -- Table-valued function
	   OR o.type = 'FN' -- Scalar function
	ORDER BY SCHEMA_NAME(o.schema_id), o.name;
OPEN function_cursor;

WHILE 1 = 1
BEGIN
	FETCH NEXT FROM function_cursor INTO @function_full_name;

	IF @@FETCH_STATUS <> 0 BREAK

	RAISERROR(N'Function %s', 0, 1, @function_full_name) WITH NOWAIT;

	-- Use @function_full_name here
END

CLOSE function_cursor;
DEALLOCATE function_cursor;
