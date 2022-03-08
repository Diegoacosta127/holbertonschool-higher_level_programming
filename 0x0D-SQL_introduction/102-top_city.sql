-- 18. Tempreatures #0
-- A script that displays the average temperature (Fahrenheit) by city ordered by tempreature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month=7 or month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3
