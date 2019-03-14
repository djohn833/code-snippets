SET NOCOUNT ON;

DECLARE @view_full_name NVARCHAR(MAX);

DECLARE view_cursor CURSOR FOR
SELECT N'[' + SCHEMA_NAME(o.schema_id) + N'].[' + o.name + N']'
FROM sys.objects o
WHERE o.type = 'V'
ORDER BY SCHEMA_NAME(o.schema_id), o.name;
OPEN view_cursor;

WHILE 1 = 1
BEGIN
	FETCH NEXT FROM view_cursor INTO @view_full_name;

	IF @@FETCH_STATUS <> 0 BREAK

	RAISERROR(N'View %s', 0, 1, @view_full_name) WITH NOWAIT;

	-- Use @view_full_name here
END

CLOSE view_cursor;
DEALLOCATE view_cursor;
