-- Create the follow table
CREATE TABLE follow (
    followee VARCHAR(100),
    follower VARCHAR(100),
    PRIMARY KEY (followee, follower)
);

-- Insert values into the follow table
INSERT INTO follow (followee, follower) VALUES
('Alice', 'Bob'),
('Bob', 'Cena'),
('Bob', 'Donald'),
('Donald', 'Edward'),
('Alice', 'David'),
('Cena', 'Fiona'),
('Donald', 'George'),
('Edward', 'Alice'),
('Bob', 'Hannah'),
('David', 'Ian');

/*
Input: 
Follow table:
+----------+----------+
| followee | follower |
+----------+----------+
| Alice    | Bob      |
| Bob      | Cena     |
| Bob      | Donald   |
| Donald   | Edward   |
+----------+----------+
Output: 
+----------+-----+
| follower | num |
+----------+-----+
| Bob      | 2   |
| Donald   | 1   |
+----------+-----+
Explanation: 
User Bob has 2 followers. Bob is a second-degree follower because he follows Alice, so we include him in the result table.
User Donald has 1 follower. Donald is a second-degree follower because he follows Bob, so we include him in the result table.
User Alice has 1 follower. Alice is not a second-degree follower because she does not follow anyone, so we don not include her in the result table.

A second-degree follower is a user who:

follows at least one user, and
is followed by at least one user.
Write a solution to report the second-degree users and the number of their followers.

Return the result table ordered by follower in alphabetical order.

The result format is in the following example.

*/

-- fetch 
select * from Follow;

WITH cte AS (
    SELECT 
        followee AS follower 
    FROM 
        Follow 
    UNION ALL
    SELECT 
        follower AS follower 
    FROM 
        Follow 
)
SELECT 
    follower,
    COUNT - 1 AS num
FROM (
    SELECT 
        follower,
        COUNT(follower) AS count
    FROM 
        cte
    GROUP BY 
        follower
) AS a
WHERE 
    count - 1 > 0
ORDER BY 
    1;
