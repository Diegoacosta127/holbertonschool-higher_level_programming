-- 13. Number of shows by genre
-- A script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each
SELECT name AS genre, COUNT(genre_id) AS number_of_shows FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.genre_id IS NOT NULL
GROUP BY genre
ORDER BY number_of_shows DESC
