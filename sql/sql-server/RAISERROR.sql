-- From https://www.sqltheater.com/blog/stop-using-print/


-- The messages print after the WAITFORs
PRINT 'The number of the bus is 2525.' 
WAITFOR DELAY '00:00:05'; 

PRINT 'It''s running downtown from Venice.' 
WAITFOR DELAY '00:00:05';


-- The messages print now, but this junks any declared variables
PRINT 'The number of the bus is 2525.'
GO
WAITFOR DELAY '00:00:05';

PRINT 'It''s running downtown from Venice.'
GO
WAITFOR DELAY '00:00:05';


-- RAISERROR to the rescue
RAISERROR('The number of the bus is 2525.', 0, 1) WITH NOWAIT;
WAITFOR DELAY '00:00:05';

RAISERROR('It''s running downtown from Venice.', 0, 1) WITH NOWAIT;
WAITFOR DELAY '00:00:05';


-- Let's try raising an actual error this time
RAISERROR('It''s running downtown from Venice.', 16, 1) WITH NOWAIT;
WAITFOR DELAY '00:00:05';


-- From https://docs.microsoft.com/en-us/sql/t-sql/language-elements/raiserror-transact-sql?view=sql-server-2017


-- Can format the message.
RAISERROR (N'This is message %s %d.', -- Message text.  
           10, -- Severity,  
           1, -- State,  
           N'number', -- First argument.  
           5); -- Second argument.  
-- The message text returned is: This is message number 5.  
GO


-- Can specify parts of the format with arguments instead of hard-coding it in the string.
RAISERROR (N'<\<%*.*s>>', -- Message text.  
           10, -- Severity,  
           1, -- State,  
           7, -- First argument used for width.  
           3, -- Second argument used for precision.  
           N'abcde'); -- Third argument supplies the string.  
-- The message text returned is: <<    abc>>.  
GO  
RAISERROR (N'<\<%7.3s>>', -- Message text.  
           10, -- Severity,  
           1, -- State,  
           N'abcde'); -- First argument supplies the string.  
-- The message text returned is: <<    abc>>.  
GO

