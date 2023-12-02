SELECT
    t1.submission_date,
    COUNT(DISTINCT t1.hacker_id) AS hkr_cnt,
    t2.hacker_id,
    h.name
FROM (
    SELECT
        p1.submission_date,
        COUNT(DISTINCT p1.hacker_id) AS hacker_cnt
    FROM (
        SELECT
            submission_date,
            hacker_id,
            ROW_NUMBER() OVER (PARTITION BY submission_date ORDER BY hacker_id) AS hacker_rank
        FROM
            (SELECT DISTINCT
                submission_date,
                hacker_id
            FROM
                submissions
            ORDER BY
                hacker_id, submission_date
            ) AS a
    ) AS p1
    JOIN (
        SELECT
            submission_date,
            ROW_NUMBER() OVER (ORDER BY submission_date) AS date_rank
        FROM
            (SELECT DISTINCT
                submission_date
            FROM
                submissions
            ORDER BY
                submission_date
            ) AS b
    ) AS p2 ON p1.submission_date = p2.submission_date AND p1.hacker_rank = p2.date_rank
    GROUP BY
        p1.submission_date
) AS t1
JOIN (
    SELECT
        submission_date,
        hacker_id,
        COUNT(*) AS sub_cnt,
        ROW_NUMBER() OVER (PARTITION BY submission_date ORDER BY COUNT(*) DESC, hacker_id) AS max_rnk
    FROM
        submissions AS s
    GROUP BY
        submission_date,
        hacker_id
) AS t2 ON t1.submission_date = t2.submission_date AND t2.max_rnk = 1
JOIN
    hackers AS h ON t2.hacker_id = h.hacker_id
ORDER BY
    t1.submission_date;
