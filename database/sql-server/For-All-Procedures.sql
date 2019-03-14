SET NOCOUNT ON;

DECLARE @procedure_full_name NVARCHAR(MAX);

DECLARE procedure_cursor CURSOR FOR
SELECT N'[' + SCHEMA_NAME(o.schema_id) + N'].[' + o.name + N']'
FROM sys.objects o
WHERE o.type = 'P'
ORDER BY SCHEMA_NAME(o.schema_id), o.name;
OPEN procedure_cursor;

WHILE 1 = 1
BEGIN
	FETCH NEXT FROM procedure_cursor INTO @procedure_full_name;

	IF @@FETCH_STATUS <> 0 BREAK

	RAISERROR(N'Procedure %s', 0, 1, @procedure_full_name) WITH NOWAIT;

	-- Use @procedure_full_name here
END

CLOSE procedure_cursor;
DEALLOCATE procedure_cursor;
