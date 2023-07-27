-- list all the cities of California that can be found in the database

SELECT cities.id states.name
FROM cities
WHERE cities.state_id = states.id
ORDER BY cities.id;
