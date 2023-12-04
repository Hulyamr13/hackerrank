SELECT
    CASE
        WHEN G.grade > 7 THEN S.name
        ELSE NULL
    END AS names,
    G.grade,
    S.marks
FROM
    students S
JOIN
    grades G ON S.marks BETWEEN G.min_mark AND G.max_mark
ORDER BY
    G.grade DESC,
    CASE
        WHEN G.grade > 7 THEN S.name
    END ASC,
    CASE
        WHEN G.grade <= 7 THEN S.marks
    END ASC;
