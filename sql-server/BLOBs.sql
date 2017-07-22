-- Export BLOB with BCP
bcp "QUERY TEXT" queryout "temp.png" -S server\instance -U username -P pw

-- Import BLOB with OPENROWSET
UPDATE [Table]
SET    [BlobValue] = (SELECT * FROM OPENROWSET(BULK 'temp.png', SINGLE_BLOB) AS x)
WHERE  [Id] = foo;
