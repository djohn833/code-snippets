USE master
GO

DECLARE @BackupDirectory nvarchar(max) = 'C:\BackupLocation';
DECLARE @VersionAndTimestamp nvarchar(max) = '';
DECLARE @backupName nvarchar(max) = @BackupDirectory + '\' + @VersionAndTimestamp + '_DatabaseName.bak';


IF EXISTS(select * from sys.databases where name='DatabaseName')
BEGIN
    ALTER DATABASE DatabaseName SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE DatabaseName;
END

--RESTORE FILELISTONLY  
--FROM DISK = @backupName;

RESTORE DATABASE DatabaseName
FROM DISK = @backupName
WITH REPLACE,
MOVE 'DatabaseName'     TO 'C:\DataDirectory\DatabaseName.mdf',
MOVE 'DatabaseName_log' TO 'C:\DataDirectory\DatabaseName_log.ldf';
