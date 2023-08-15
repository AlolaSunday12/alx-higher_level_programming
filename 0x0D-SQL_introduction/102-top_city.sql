-- displays the average temp of 3 cities
-- during July and August
-- ordered by temperature desc

SELECT city, AVG(temp) AS avg_temp
FROM weather_data
WHERE (month = 7 OR month = 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
