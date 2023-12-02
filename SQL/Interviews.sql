SELECT
    con.contest_id,
    con.hacker_id,
    con.name,
    COALESCE(SUM(ss.total_submissions), 0) AS total_submissions,
    COALESCE(SUM(ss.total_accepted_submissions), 0) AS total_accepted_submissions,
    COALESCE(SUM(vs.total_views), 0) AS total_views,
    COALESCE(SUM(vs.total_unique_views), 0) AS total_unique_views
FROM
    contests con
JOIN
    colleges col ON con.contest_id = col.contest_id
JOIN
    challenges cha ON col.college_id = cha.college_id
LEFT JOIN (
    SELECT
        challenge_id,
        SUM(total_views) AS total_views,
        SUM(total_unique_views) AS total_unique_views
    FROM
        view_stats
    GROUP BY
        challenge_id
) vs ON cha.challenge_id = vs.challenge_id
LEFT JOIN (
    SELECT
        challenge_id,
        SUM(total_submissions) AS total_submissions,
        SUM(total_accepted_submissions) AS total_accepted_submissions
    FROM
        submission_stats
    GROUP BY
        challenge_id
) ss ON cha.challenge_id = ss.challenge_id
GROUP BY
    con.contest_id,
    con.hacker_id,
    con.name
HAVING
    SUM(COALESCE(ss.total_submissions, 0)) != 0 OR
    SUM(COALESCE(ss.total_accepted_submissions, 0)) != 0 OR
    SUM(COALESCE(vs.total_views, 0)) != 0 OR
    SUM(COALESCE(vs.total_unique_views, 0)) != 0
ORDER BY
    contest_id;
