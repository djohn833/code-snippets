USE [master]

DECLARE @BackupDirectory nvarchar(max) = 'C:\Share';

DECLARE @timestamp datetime = CURRENT_TIMESTAMP;
DECLARE @timestampString char(12) = FORMAT(@timestamp, 'yyyyMMddHHmm');
DECLARE @timestampDisplayString char(16) = FORMAT(@timestamp, 'yyyy-MM-dd HH:mm');
DECLARE @version nvarchar(64) = (SELECT CONVERT(nvarchar(64), value) FROM [DatabaseName]..fn_listextendedproperty('Version', default, default, default, default, default, default));
DECLARE @databaseVersion nvarchar(max) = DatabaseProperty('DatabaseName','version');
DECLARE @backupName nvarchar(max) = @BackupDirectory + '\' + @version + '_' + @timestampString + '_' + @databaseVersion + '_DatabaseName.bak';

RAISERROR('Backing up Database Version %s at %s', 0, 1, @version, @timestampDisplayString) WITH NOWAIT;

RAISERROR('Backing up DatabaseName to %s', 0, 1, @backupName) WITH NOWAIT;

BACKUP DATABASE [DatabaseName]
TO DISK = @backupName
WITH INIT, COPY_ONLY, STATS;
