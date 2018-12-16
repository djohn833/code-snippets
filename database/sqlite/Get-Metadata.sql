-- Dump all table definitions
-- Use for dumping into a file or listing at a command prompt
SELECT GROUP_CONCAT(sql, CHAR(13, 10)) FROM sqlite_master WHERE type='table';

-- Use in SQL injection
SELECT GROUP_CONCAT(sql, '<br/>') FROM sqlite_master WHERE type='table';
