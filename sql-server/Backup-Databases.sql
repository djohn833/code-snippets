DECLARE @BackupDirectory nvarchar(max) = 'C:\BackupLocation';
DECLARE @timestamp datetime = CURRENT_TIMESTAMP;
DECLARE @timestampString char(12) = FORMAT(@timestamp, 'yyyyMMddHHmm');
DECLARE @version nvarchar(64);
DECLARE @backupName nvarchar(max);

USE [DatabaseName]
SELECT @version = CONVERT(nvarchar(64), value) FROM fn_listextendedproperty('Version', default, default, default, default, default, default);

SET @backupName = @BackupDirectory + '\' + @version + '_' + @timestampString + '_DatabaseName.bak';


USE [master]

PRINT('Backing up Database Version ' + @version + ' at ' + FORMAT(@timestamp, 'yyyy-MM-dd HH:mm'));

PRINT('Backing up DatabaseName to ' + @backupName);

BACKUP DATABASE [DatabaseName]
TO DISK = @backupName
WITH INIT, STATS;
