-- Lists all genres not linked to the show "Dexter"
SELECT g.`name`
FROM `tv_genres` AS g
WHERE g.`id` NOT IN (
    SELECT t.`genre_id`
    FROM `tv_show_genres` AS t
    INNER JOIN `tv_shows` AS s ON t.`show_id` = s.`id`
    WHERE s.`title` = 'Dexter'
)
ORDER BY g.`name`;
