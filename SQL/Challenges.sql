WITH challenge_counts AS (
    SELECT DISTINCT
        h.hacker_id,
        h.name,
        COUNT(c.challenge_id) OVER(PARTITION BY c.hacker_id) AS num_challenges
    FROM
        Hackers h JOIN Challenges c ON h.hacker_id = c.hacker_id
), max_challenge_count AS (
    SELECT MAX(num_challenges) AS maxn
    FROM challenge_counts
), duplicate AS (
    SELECT num_challenges AS dups_num_chal
    FROM challenge_counts
    GROUP BY num_challenges
    HAVING COUNT(*) > 1
)
SELECT
    *
FROM
    challenge_counts
WHERE
    num_challenges = (SELECT maxn FROM max_challenge_count)
    OR
    num_challenges NOT IN (SELECT dups_num_chal FROM duplicate)
ORDER BY
    num_challenges DESC,
    hacker_id;
