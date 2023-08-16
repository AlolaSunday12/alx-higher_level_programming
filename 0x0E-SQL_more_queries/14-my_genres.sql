-- Lists all genres of the show Dexter from the hbtn_0d_tvshows database.
-- Each record displays the genre name.
-- Results are sorted in ascending order by genre name.

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- List genres of the show Dexter
SELECT g.name
FROM tv_shows AS s
JOIN tv_show_genres AS sg ON s.id = sg.show_id
JOIN tv_genres AS g ON sg.genre_id = g.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
