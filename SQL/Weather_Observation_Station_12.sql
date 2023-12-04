SELECT DISTINCT CITY
FROM STATION
WHERE NOT ((LEFT(CITY, 1) IN ('A', 'E', 'I', 'O', 'U') OR LEFT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u'))
           OR (RIGHT(CITY, 1) IN ('A', 'E', 'I', 'O', 'U') OR RIGHT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u')));
