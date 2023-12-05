SELECT ROUND(AVG(Lat_N), 4)
FROM (
    SELECT Lat_N, ROW_NUMBER() OVER (ORDER BY Lat_N) AS row_num,
           COUNT(*) OVER () AS total_rows
    FROM Station
) AS Temp
WHERE row_num = CEIL(total_rows / 2.0) OR
      row_num = FLOOR(total_rows / 2.0) + 1;
