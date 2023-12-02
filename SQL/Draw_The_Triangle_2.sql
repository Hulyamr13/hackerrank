WITH RECURSIVE Pattern AS (
    SELECT 1 AS num, '* ' AS pattern
    UNION ALL
    SELECT num + 1, pattern || '* ' AS pattern
    FROM Pattern
    WHERE num < 20
)
SELECT pattern
FROM Pattern;
