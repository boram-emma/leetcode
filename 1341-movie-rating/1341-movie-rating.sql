# Write your MySQL query statement below

# Find the name of the user who has rated the greatest number of movies
# In case of a tie, return the lexicographically smaller user name. ??

# Find the movie name with the highest average rating in February 2020.
# In case of a tie, return the lexicographically smaller movie name. ??

SELECT results
FROM (
    (
    SELECT sub.name AS results
    FROM
        (SELECT u.name, count(m.user_id) AS count
        FROM Users u
        LEFT JOIN MovieRating m ON u.user_id = m.user_id
        GROUP BY u.user_id) AS sub
    ORDER BY sub.count DESC, sub.name ASC
    LIMIT 1
    )
    UNION ALL
    (
    SELECT m.title AS results
    FROM Movies m
    LEFT JOIN MovieRating mr ON m.movie_id = mr.movie_id 
    WHERE mr.created_at BETWEEN '2020-02-01' AND '2020-02-28' 
    GROUP BY m.movie_id
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
    )
) AS final_result;