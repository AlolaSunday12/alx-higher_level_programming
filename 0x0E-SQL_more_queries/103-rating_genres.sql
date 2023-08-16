-- List all genres in the database hbtn_0d_tvshows_rate by their rating sum

-- List genres and their rating sum, sorted by rating sum in descending order
SELECT tg.name, SUM(tr.rate) AS rating_sum
FROM tv_genres AS tg
JOIN tv_show_genres AS tsg ON tg.id = tsg.genre_id
JOIN tv_show_ratings AS tr ON tsg.show_id = tr.show_id
GROUP BY tg.name
ORDER BY rating_sum DESC;
