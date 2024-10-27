
-- create
CREATE TABLE Employee (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    experience_years INT
);

CREATE TABLE Project (
    project_id INT,
    employee_id INT
);

-- insert
INSERT INTO Employee (employee_id, name, experience_years) VALUES
(1, 'Khaled', 3),
(2, 'Ali', 2),
(3, 'John', 3),
(4, 'Doe', 2);

INSERT INTO Project (project_id, employee_id) VALUES
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(2, 4);

/*
Input: 
Project table:
+-------------+-------------+
| project_id  | employee_id |
+-------------+-------------+
| 1           | 1           |
| 1           | 2           |
| 1           | 3           |
| 2           | 1           |
| 2           | 4           |
+-------------+-------------+
Employee table:
+-------------+--------+------------------+
| employee_id | name   | experience_years |
+-------------+--------+------------------+
| 1           | Khaled | 3                |
| 2           | Ali    | 2                |
| 3           | John   | 3                |
| 4           | Doe    | 2                |
+-------------+--------+------------------+
Output: 
+-------------+---------------+
| project_id  | employee_id   |
+-------------+---------------+
| 1           | 1             |
| 1           | 3             |
| 2           | 1             |
+-------------+---------------+
Explanation: Both employees with id 1 and 3 have the most experience among the employees of the first project. For the second project, the employee with id 1 has the most experience.


Write a solution to report the most experienced employees in each project. 
In case of a tie, report all employees with the maximum number of experience years.

Return the result table in any order.
*/

SELECT
    p.project_id,
    e.employee_id
FROM
    Project AS p
INNER JOIN
    Employee AS e ON p.employee_id = e.employee_id
WHERE
    (p.project_id, e.experience_years) IN (
        SELECT
            p.project_id,
            MAX(e.experience_years) AS max_exp_years
        FROM
            Project AS p
        INNER JOIN
            Employee AS e ON p.employee_id = e.employee_id
        GROUP BY
            p.project_id
    )
GROUP BY
    p.project_id,
    e.employee_id;
