-- Lists all shows and their linked genres from the hbtn_0d_tvshows database.
-- Displays NULL if a show doesn’t have a genre.
-- Each record displays the show title and genre name.
-- Results are sorted in ascending order by show title and genre name.

-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- List shows and linked genres
SELECT s.title, g.name
FROM tv_shows AS s
LEFT JOIN tv_show_genres AS sg ON s.id = sg.show_id
LEFT JOIN tv_genres AS g ON sg.genre_id = g.id
ORDER BY s.title ASC, g.name ASC;
