-- Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows linked to each.
-- Does not display genres without linked shows.
-- Records are ordered by descending number of shows linked.

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- List genres and the number of shows linked to each
SELECT g.name AS genre, COUNT(tsg.genre_id) AS number_of_shows
FROM tv_genres AS g
INNER JOIN tv_show_genres AS tsg ON g.id = tsg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
