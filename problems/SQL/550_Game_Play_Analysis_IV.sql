-- create
CREATE TABLE Activity (
    player_id INT,
    device_id INT,
    event_date DATE,
    games_played INT,
);


-- insert
INSERT INTO Activity (player_id, device_id, event_date, games_played) VALUES
(1, 2, '2016-03-01', 5),
(1, 2, '2016-03-02', 6),
(2, 3, '2017-06-25', 1),
(3, 1, '2016-03-02', 0),
(3, 4, '2018-07-03', 5);

/*
Input: 
Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+
Output: 
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
Explanation: 
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33
*/

WITH base_table AS (
    SELECT
        a1.player_id,
        MIN(a1.event_date) OVER (PARTITION BY a1.player_id ORDER BY a1.event_date) AS first_login_date,
        MIN(a2.event_date) OVER (PARTITION BY a2.player_id ORDER BY a2.event_date) AS second_login_date
    FROM
        Activity AS a1
    LEFT JOIN
        Activity AS a2 ON a1.player_id = a2.player_id AND a1.event_date = a2.event_date - INTERVAL '1 day'
    ORDER BY
        a1.event_date ASC
),

next_day_flag AS (
    SELECT
        player_id,
        CASE
            WHEN MIN(first_login_date) + INTERVAL '1 day' = MIN(second_login_date) THEN 1
            ELSE NULL
        END AS next_day_login_flag
    FROM
        base_table
    GROUP BY
        player_id
)

SELECT
    ROUND(COUNT(next_day_login_flag) * 1.0 / COUNT(DISTINCT player_id), 2) AS fraction
FROM
    next_day_flag;
