-- No default
IF COL_LENGTH(N'[SchemaName].[TableName]', N'NewColumnName') IS NULL
BEGIN
    PRINT N'Adding [SchemaName].[TableName].[NewColumnName]'
    ALTER TABLE [SchemaName].[TableName] ADD [NewColumnName] [NewColumnType] NOT NULL;
END

-- With default
IF COL_LENGTH(N'[SchemaName].[TableName]', N'NewColumnName') IS NULL
BEGIN
    PRINT N'Adding [SchemaName].[TableName].[NewColumnName]'
    ALTER TABLE [SchemaName].[TableName] ADD [NewColumnName] [NewColumnType] NOT NULL CONSTRAINT [DF_TableName_NewColumnName] DEFAULT ((0))
END
