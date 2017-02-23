-- ultimate destination: 
-- email / movie title for users who have given a 5 
-- rating to three or more movies


-- user_id for any users who have given any movie a score of 5
SELECT DISTINCT user_id
FROM ratings
WHERE score = 5;

-- email for any users who have give any movie a score of 5

SELECT DISTINCT (u.user_id, u.email)
FROM ratings AS r
    JOIN users AS u
    USING(user_id)
    -- ON r.user_id = u.user_id
WHERE score = 5;

-- email for any users who have given at least 3 movies a score of 5
SELECT DISTINCT (u.user_id, u.email)
FROM ratings AS r
    JOIN users AS u
    USING(user_id)
    -- ON r.user_id = u.user_id
WHERE score = 5
GROUP BY u.user_id
HAVING COUNT(rating_id) >= 3;

-- email / movie title for users who have given a 5 
-- rating to three or more movies

SELECT DISTINCT (u.user_id, u.email)
FROM ratings AS r
    JOIN users AS u
    USING(user_id)
    -- ON r.user_id = u.user_id
WHERE score = 5
GROUP BY u.user_id
HAVING COUNT(rating_id) >= 3;










