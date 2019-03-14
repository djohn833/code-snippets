SET NOCOUNT ON;

DECLARE @table_full_name NVARCHAR(MAX);

DECLARE table_cursor CURSOR FOR
SELECT N'[' + SCHEMA_NAME(o.schema_id) + N'].[' + o.name + N']'
FROM sys.objects o
WHERE o.type = 'U'
ORDER BY SCHEMA_NAME(o.schema_id), o.name;
OPEN table_cursor;

WHILE 1 = 1
BEGIN
	FETCH NEXT FROM table_cursor INTO @table_full_name;

	IF @@FETCH_STATUS <> 0 BREAK

	RAISERROR(N'Table %s', 0, 1, @table_full_name) WITH NOWAIT;

	-- Use @table_full_name here
END

CLOSE table_cursor;
DEALLOCATE table_cursor;
