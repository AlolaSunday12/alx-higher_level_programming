-- list all cities with their corresponding state names using a JOIN
-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- List all cities with corresponding state names using a JOIN
SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
