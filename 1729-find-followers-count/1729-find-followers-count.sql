# Write your MySQL query statement below

# EACH USER
# RETURN THE NUMBER OF FOLLOWERS
# ORDERED BY USER_ID

SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id