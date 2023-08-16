-- Lists all shows without the genre "Comedy"
SELECT s.`title`
FROM `tv_shows` AS s
WHERE s.`id` NOT IN (
    SELECT t.`show_id`
    FROM `tv_show_genres` AS t
    WHERE t.`genre_id` = (
        SELECT g.`id`
        FROM `tv_genres` AS g
        WHERE g.`name` = 'Comedy'
    )
)
ORDER BY s.`title`;
