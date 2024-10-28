-- Create the Teams table
CREATE TABLE Teams (
    team_id INT PRIMARY KEY,
    team_name VARCHAR(50)
);

-- Create the Matches table
CREATE TABLE Matches (
    match_id INT PRIMARY KEY,
    host_team INT,
    guest_team INT,
    host_goals INT,
    guest_goals INT,
    FOREIGN KEY (host_team) REFERENCES Teams(team_id),
    FOREIGN KEY (guest_team) REFERENCES Teams(team_id)
);


-- Insert data into the Teams table
INSERT INTO Teams (team_id, team_name) VALUES
(10, 'Leetcode FC'),
(20, 'NewYork FC'),
(30, 'Atlanta FC'),
(40, 'Chicago FC'),
(50, 'Toronto FC');


-- Insert data into the Matches table
INSERT INTO Matches (match_id, host_team, guest_team, host_goals, guest_goals) VALUES
(1, 10, 20, 3, 0),
(2, 30, 10, 2, 2),
(3, 10, 50, 5, 1),
(4, 20, 30, 1, 0),
(5, 50, 30, 1, 0);

/*
Input: 
Teams table:
+-----------+--------------+
| team_id   | team_name    |
+-----------+--------------+
| 10        | Leetcode FC  |
| 20        | NewYork FC   |
| 30        | Atlanta FC   |
| 40        | Chicago FC   |
| 50        | Toronto FC   |
+-----------+--------------+
Matches table:
+------------+--------------+---------------+-------------+--------------+
| match_id   | host_team    | guest_team    | host_goals  | guest_goals  |
+------------+--------------+---------------+-------------+--------------+
| 1          | 10           | 20            | 3           | 0            |
| 2          | 30           | 10            | 2           | 2            |
| 3          | 10           | 50            | 5           | 1            |
| 4          | 20           | 30            | 1           | 0            |
| 5          | 50           | 30            | 1           | 0            |
+------------+--------------+---------------+-------------+--------------+
Output: 
+------------+--------------+---------------+
| team_id    | team_name    | num_points    |
+------------+--------------+---------------+
| 10         | Leetcode FC  | 7             |
| 20         | NewYork FC   | 3             |
| 50         | Toronto FC   | 3             |
| 30         | Atlanta FC   | 1             |
| 40         | Chicago FC   | 0             |
+------------+--------------+---------------+

You would like to compute the scores of all teams after all matches. Points are awarded as follows:
- A team receives three points if they win a match (i.e., Scored more goals than the opponent team).
- A team receives one point if they draw a match (i.e., Scored the same number of goals as the opponent team).
- A team receives no points if they lose a match (i.e., Scored fewer goals than the opponent team).

Write a solution that selects the team_id, team_name and num_points of each team in the tournament after all described matches.

Return the result table ordered by num_points in decreasing order. In case of a tie, order the records by team_id in increasing order.

*/

-- fetch 
select * from Teams;
select * from Matches;


WITH host_team AS (
    SELECT
        host_team,
        CASE
            WHEN host_goals > guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS points_scored
    FROM Matches
),

guest_team AS (
    SELECT
        guest_team,
        CASE
            WHEN host_goals < guest_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END AS points_scored
    FROM Matches
),

total_score AS (
    SELECT * FROM host_team
    UNION ALL
    SELECT * FROM guest_team
)

SELECT
    t.team_id,
    t.team_name,
    COALESCE(SUM(points_scored), 0) AS num_points
FROM total_score AS ts
RIGHT JOIN Teams AS t ON t.team_id = ts.host_team
GROUP BY 
    t.team_id,
    t.team_name
ORDER BY 
    COALESCE(SUM(points_scored), 0) DESC,
    t.team_id ASC;


----- Simpler Solution ------
SELECT
    team_id,
    team_name,
    SUM(
        CASE
            WHEN team_id = host_team
            AND host_goals > guest_goals THEN 3
            WHEN team_id = guest_team
            AND guest_goals > host_goals THEN 3
            WHEN host_goals = guest_goals THEN 1
            ELSE 0
        END
    ) AS num_points
FROM
    Teams
    LEFT JOIN Matches ON team_id = host_team OR team_id = guest_team
GROUP BY 1
ORDER BY 3 DESC, 1;