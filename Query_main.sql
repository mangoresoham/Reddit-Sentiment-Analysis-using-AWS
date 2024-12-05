WITH all_sentiments AS (
    SELECT 'POSITIVE' AS sentiment
    UNION ALL
    SELECT 'NEGATIVE'
    UNION ALL
    SELECT 'NEUTRAL'
    UNION ALL
    SELECT 'MIXED'
)
SELECT
    UPPER(s.sentiment) AS sentiment,
    COUNT(d.sentiment) AS count
FROM
    all_sentiments s
LEFT JOIN
    "sampledb"."data" d ON UPPER(s.sentiment) = UPPER(d.sentiment)
GROUP BY
    UPPER(s.sentiment);