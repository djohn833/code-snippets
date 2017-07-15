-- [.character.] is a way to escape any character.
-- It even supports special names, which is particularly
-- useful for nonprinting characters (e.g., [.NUL.]).
SELECT '~' REGEXP BINARY '^[[.~.]]';

-- [.character.] can also be used for endpoints of ranges.
-- This is useful for writing a binary search with blind
-- SQL injection, since the regex will work without extra
-- logic to escape some special characters.
SELECT 'abc' REGEXP BINARY '^ab[[.b.]-[.d.]]';

