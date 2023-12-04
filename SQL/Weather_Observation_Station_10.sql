SELECT DISTINCT CITY
FROM STATION
WHERE NOT (RIGHT(CITY, 1) IN ('A', 'E', 'I', 'O', 'U') OR RIGHT(CITY, 1) IN ('a', 'e', 'i', 'o', 'u'));
