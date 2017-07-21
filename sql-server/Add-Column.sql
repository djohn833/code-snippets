IF COL_LENGTH(N'[Schema].[Table]', N'NewColumn') IS NULL
BEGIN
    PRINT N'Adding [Schema].[Table].[NewColumn]'
    ALTER TABLE [Schema].[Table] ADD [NewColumn] [ColumnType];
END
