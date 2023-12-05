SELECT string_agg(CAST(NUMB AS VARCHAR), '&') AS primes
FROM (
    SELECT generate_series(2, 1000) AS NUMB
) tempNum
WHERE NOT EXISTS (
    SELECT 1
    FROM generate_series(2, tempNum.NUMB / 2) AS NUMA
    WHERE tempNum.NUMB % NUMA = 0
);
