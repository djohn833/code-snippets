-- Use FOR XML and STUFF to join strings
DECLARE @separator varchar(10) = ', ';
DECLARE @separatorLength tinyint = LEN(REPLACE(@separator, ' ', '*')); -- BEWARE! LEN does not count trailing spaces, so we can't just use LEN(@separator).

SELECT
	 parent.id
	,STUFF(joinStrings.value, 1, @separatorLength, '') AS joinStringsValue
FROM (VALUES (1), (2), (3)) parent(id)
OUTER APPLY
	(
		SELECT @separator + children.value
		FROM (VALUES (1, 'Foo'), (1, 'Bar'), (2, 'Baz'), (3, 'Quux')) children(id, value)
		WHERE children.id = parent.id
		FOR XML PATH('')
	) AS joinStrings(value)
