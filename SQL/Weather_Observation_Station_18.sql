SELECT ROUND(ABS(A - B) + ABS(C - D), 4)
FROM (
    SELECT MAX(LAT_N) AS A, MIN(LAT_N) AS B, MAX(LONG_W) AS C, MIN(LONG_W) AS D
    FROM STATION
) AS T;
