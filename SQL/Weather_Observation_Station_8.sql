SELECT DISTINCT CITY
FROM STATION
WHERE (LEFT(CITY, 1) IN ('A', 'E', 'I', 'O', 'U') OR LEFT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u'))
  AND (RIGHT(CITY, 1) IN ('A', 'E', 'I', 'O', 'U') OR RIGHT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u'));
