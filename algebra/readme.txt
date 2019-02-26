Working on a way of categorizing different algebraic structures.

Use this to dump the schema and data:
pg_dump math > math.sql

Restore the data with psql:
CREATE DATABASE math;
\c math
\i math.sql

