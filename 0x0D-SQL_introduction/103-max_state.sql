-- display max tempretature of each state
-- order by statename

SELECT state, MAX(temp) AS max_temp
FROM weather_data
GROUP BY state
ORDER BY state;
