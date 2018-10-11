DECLARE @version varchar(64);

USE [DatabaseName]
SELECT @version = CONVERT(varchar(64), value)
FROM fn_listextendedproperty('Version', default, default, default, default, default, default);

USE [master]

PRINT('Version: ' + @version)
