-- No default
IF COL_LENGTH(N'[SchemaName].[TableName]', N'NewColumnName') IS NULL
BEGIN
    PRINT N'Adding [SchemaName].[TableName].[NewColumnName]'
    ALTER TABLE [SchemaName].[TableName] ADD [NewColumnName] [NewColumnType];
END

-- With default
IF COL_LENGTH(N'[SchemaName].[TableName]', N'NewColumnName') IS NULL
BEGIN
    PRINT N'Adding [SchemaName].[TableName].[NewColumnName]'
    ALTER TABLE [SchemaName].[TableName] ADD [NewColumnName] [NewColumnType] CONSTRAINT [DF_TableName_NewColumnName] DEFAULT ((0))
END
