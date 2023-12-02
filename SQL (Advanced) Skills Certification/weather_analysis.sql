SELECT
    MONTH(record_date) AS month,
    MAX(CASE WHEN data_type = 'max' THEN data_value ELSE NULL END) AS max_value,
    MIN(CASE WHEN data_type = 'min' THEN data_value ELSE NULL END) AS min_value,
    ROUND(AVG(CASE WHEN data_type = 'avg' THEN CAST(data_value AS FLOAT) ELSE NULL END), 0) AS avg_value
FROM temperature_records
GROUP BY MONTH(record_date)
ORDER BY month;