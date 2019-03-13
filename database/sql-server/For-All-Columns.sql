SET NOCOUNT ON;

DECLARE column_cursor CURSOR FOR
	SELECT N'[' + SCHEMA_NAME(tables.schema_id) + N'].[' + OBJECT_NAME(all_columns.object_id) + N']', all_columns.name
	FROM sys.all_columns
	JOIN sys.tables ON tables.object_id = all_columns.object_id
	ORDER BY SCHEMA_NAME(tables.schema_id), OBJECT_NAME(all_columns.object_id), all_columns.name;
OPEN column_cursor;

DECLARE @MatchingColumns TABLE (
	TableFullName NVARCHAR(MAX),
	ColumnName SYSNAME
);

WHILE 1 = 1
BEGIN
	DECLARE @table_full_name NVARCHAR(MAX), @column_name SYSNAME, @match BIT;

	FETCH NEXT FROM column_cursor INTO @table_full_name, @column_name;

	IF @@FETCH_STATUS <> 0 BREAK

	RAISERROR(N'Table %s, Column %s', 0, 1, @table_full_name, @column_name) WITH NOWAIT;

	-- Use @table_full_name and @column_name here

	-- For example, find columns with values that match a certain criteria.
	DECLARE @sql NVARCHAR(MAX) = N'IF EXISTS(SELECT TOP 1 0 FROM ' + @table_full_name + ' WHERE CONVERT(VARCHAR(MAX), ' + @column_name + ') LIKE ''%StringToFind%'') SELECT @match = 1;';
	EXEC sp_executesql @sql,
		N'@table_full_name NVARCHAR(MAX), @column_name SYSNAME, @match BIT OUTPUT',
		@table_full_name = @table_full_name,
		@column_name = @column_name,
		@match = @match OUTPUT;

	IF @match = 1
	BEGIN
		INSERT INTO @MatchingColumns (TableFullName, ColumnName) VALUES (@table_full_name, @column_name);
	END
END

CLOSE column_cursor;
DEALLOCATE column_cursor;

RAISERROR(N'Finished', 0, 1) WITH NOWAIT;

SELECT mc.TableFullName, mc.ColumnName
FROM @MatchingColumns mc;
