-- a script that lists all cities contained in the database

SELECT c.id, c.name, s.name
FROM cities c
LEFT JOIN states s
    ON c.state_id = s.id;
