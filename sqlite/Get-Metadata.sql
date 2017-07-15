-- Dump all table definitions
-- Use for dumping into a file or listing at a command prompt
select group_concat(sql, char(13, 10)) from sqlite_master where type='table';

-- Use in SQL injection
select group_concat(sql, '<br/>') from sqlite_master where type='table';
