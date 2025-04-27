# Write your MySQL query statement below
-- SELECT user_id, name, mail
-- FROM Users
-- WHERE mail REGEXP '@leetcode.com$' AND mail REGEXP '^[A-Za-z0-9_.\\-@]+$' AND mail REGEXP '^[A-Za-z]'

SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[A-Za-z][A-Za-z0-9_.\\-]*@leetcode\\.com$'

# 1. having REGEXP '@leetcode$'
# 2. '^[A-Za-z0-9_.-@]+$'
# 3. '^[A-Za-z]'
--  AND mail REGEXP '^[A-Za-z0-9_.-@]+$'
--   AND '^[A-Za-z]';