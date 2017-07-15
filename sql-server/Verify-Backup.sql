USE master
GO

DECLARE @BackupDirectory nvarchar(max) = 'C:\BackupLocation';
DECLARE @VersionAndTimestamp nvarchar(max) = 'version_timestamp';
DECLARE @backupName nvarchar(max) = @BackupDirectory + '\' + @VersionAndTimestamp + '_DatabaseName.bak';


IF EXISTS(select * from sys.databases where name='TestDatabaseName')
BEGIN
	ALTER DATABASE TestDatabaseName SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
	DROP DATABASE TestDatabaseName;
END

RESTORE DATABASE TestDatabaseName
FROM DISK = @backupName
WITH REPLACE,
MOVE 'DatabaseName'     TO 'C:\DataDirectory\DatabaseName.mdf',
MOVE 'DatabaseName_log' TO 'C:\DataDirectory\DatabaseName_log.ldf';

DBCC CHECKDB (TestDatabaseName) WITH NO_INFOMSGS;
