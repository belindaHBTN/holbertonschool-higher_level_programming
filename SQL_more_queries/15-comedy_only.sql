-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT s.title
FROM tv_show_genres sg
JOIN tv_shows s
    ON sg.show_id = s.id
JOIN tv_genres g
    ON sg.genre_id = g.id
WHERE g.name = "Comedy"
ORDER BY s.title;
