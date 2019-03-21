CREATE FUNCTION [dbo].[ToDotNetStringLiteral]
(	
	@value NVARCHAR(MAX)
)
RETURNS NVARCHAR(MAX)
AS
BEGIN
	RETURN N'@"' + REPLACE(@value, '"', '""') + N'"';
END