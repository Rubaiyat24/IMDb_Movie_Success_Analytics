#test

SELECT *
FROM movies_clean
LIMIT 10;

/*
Business Question 1
Which movie genres receive the highest audience ratings?
*/

SELECT
    primary_genre,
    COUNT(*) AS total_movies,
    ROUND(AVG(vote_average),2) AS average_rating

FROM movies_clean

WHERE
    vote_average > 0
    AND vote_count >= 100
    AND primary_genre IS NOT NULL

GROUP BY primary_genre

HAVING COUNT(*) >= 20

ORDER BY average_rating DESC;

/*
Business Question 2
Which genres generate the highest average revenue?
*/

SELECT
    primary_genre,
    COUNT(*) AS total_movies,
    ROUND(AVG(revenue),2) AS average_revenue,
    ROUND(SUM(revenue),2) AS total_revenue

FROM movies_clean

WHERE
    revenue > 0
    AND primary_genre IS NOT NULL

GROUP BY primary_genre

HAVING COUNT(*) >= 20

ORDER BY average_revenue DESC;

/*
Business Question 3
Which movies generated the highest revenue?
*/

SELECT
    title,
    primary_genre,
    revenue,
    budget,
    vote_average

FROM movies_clean

WHERE revenue > 0

ORDER BY revenue DESC

LIMIT 10;

/*
Business Question 4
Which movies achieved the highest ROI?
*/

SELECT
    title,
    primary_genre,
    budget,
    revenue,
    estimated_profit,
    ROUND(roi_percentage,2) AS roi_percentage

FROM movies_clean

WHERE
    budget > 1000000
    AND revenue > 0

ORDER BY roi_percentage DESC

LIMIT 10;

/*
Business Question 5
Do longer movies receive higher ratings?
*/

SELECT
CASE
WHEN runtime < 90 THEN 'Short'
WHEN runtime BETWEEN 90 AND 120 THEN 'Medium'
WHEN runtime BETWEEN 121 AND 150 THEN 'Long'
ELSE 'Very Long'
END AS movie_length,
COUNT(*) AS total_movies,
ROUND(AVG(vote_average),2) AS average_rating
FROM movies_clean
WHERE
runtime >0
AND vote_count>=100
GROUP BY movie_length
ORDER BY average_rating DESC;

/*
Business Question 6
How have movie ratings changed over time?
*/

SELECT release_year,
COUNT(*) AS total_movies,
ROUND(AVG(vote_average),2) AS average_rating
FROM movies_clean
WHERE
release_year IS NOT NULL
AND vote_count>=100
GROUP BY release_year
HAVING COUNT(*)>=20
ORDER BY release_year;


/*
Business Question 7
Which movies generated the highest audience engagement?
*/

SELECT
title,
primary_genre,
vote_count,
vote_average,
ROUND(popularity,2) AS popularity
FROM movies_clean
WHERE vote_count>0
ORDER BY vote_count DESC
LIMIT 10;

/*
Business Question 8
Which highly popular movies received poor ratings?
*/

SELECT
title,
primary_genre,
ROUND(popularity,2) AS popularity,
vote_average,
vote_count
FROM movies_clean
WHERE
popularity>=20
AND vote_average<5
AND vote_count>=100
ORDER BY popularity DESC
LIMIT 20;

