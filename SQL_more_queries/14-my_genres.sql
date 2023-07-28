-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

SELECT g.name
FROM tv_show_genres sg
JOIN tv_shows s
    ON sg.show_id = s.id
JOIN tv_genres g
    ON sg.genre_id = g.id
WHERE s.title = "Dexter"
ORDER BY g.name;
