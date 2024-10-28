-- Create the Transactions table
CREATE TABLE Transactions (
    id INT PRIMARY KEY,
    country VARCHAR(2),
    state VARCHAR(10),
    amount DECIMAL(10, 2),
    trans_date DATE
);

-- Create the Chargebacks table
CREATE TABLE Chargebacks (
    trans_id INT,
    trans_date DATE,
    PRIMARY KEY (trans_id),
    FOREIGN KEY (trans_id) REFERENCES Transactions(id)
);

-- Insert data into the Transactions table
INSERT INTO Transactions (id, country, state, amount, trans_date) VALUES
(101, 'US', 'approved', 1000.00, '2019-05-18'),
(102, 'US', 'declined', 2000.00, '2019-05-19'),
(103, 'US', 'approved', 3000.00, '2019-06-10'),
(104, 'US', 'declined', 4000.00, '2019-06-13'),
(105, 'US', 'approved', 5000.00, '2019-06-15');


-- Insert data into the Chargebacks table
INSERT INTO Chargebacks (trans_id, trans_date) VALUES
(102, '2019-05-29'),
(101, '2019-06-30'),
(105, '2019-09-18');

/*
Input: 
Transactions table:
+-----+---------+----------+--------+------------+
| id  | country | state    | amount | trans_date |
+-----+---------+----------+--------+------------+
| 101 | US      | approved | 1000   | 2019-05-18 |
| 102 | US      | declined | 2000   | 2019-05-19 |
| 103 | US      | approved | 3000   | 2019-06-10 |
| 104 | US      | declined | 4000   | 2019-06-13 |
| 105 | US      | approved | 5000   | 2019-06-15 |
+-----+---------+----------+--------+------------+
Chargebacks table:
+----------+------------+
| trans_id | trans_date |
+----------+------------+
| 102      | 2019-05-29 |
| 101      | 2019-06-30 |
| 105      | 2019-09-18 |
+----------+------------+
Output: 
+---------+---------+----------------+-----------------+------------------+-------------------+
| month   | country | approved_count | approved_amount | chargeback_count | chargeback_amount |
+---------+---------+----------------+-----------------+------------------+-------------------+
| 2019-05 | US      | 1              | 1000            | 1                | 2000              |
| 2019-06 | US      | 2              | 8000            | 1                | 1000              |
| 2019-09 | US      | 0              | 0               | 1                | 5000              |
+---------+---------+----------------+-----------------+------------------+-------------------+

Write a solution to find for each month and country: the number of approved transactions and their total amount, 
the number of chargebacks, and their total amount.

Note: In your solution, given the month and country, ignore rows with all zeros.

Return the result table in any order.


*/

-- fetch 
select * from Transactions;
select * from Chargebacks;

WITH
    combined AS (
        SELECT * FROM Transactions
        UNION
        SELECT id, country, 'chargeback', amount, c.trans_date
        FROM
            Transactions AS t
            JOIN Chargebacks AS c ON t.id = c.trans_id
    )

SELECT
    TO_CHAR(trans_date, 'YYYY-MM') AS month,
    country,
    SUM(CASE WHEN state = 'approved' THEN 1 ELSE 0 END) AS approved_count,
    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_amount,
    SUM(CASE WHEN state = 'chargeback' THEN 1 ELSE 0 END) AS chargeback_count,
    SUM(CASE WHEN state = 'chargeback' THEN amount ELSE 0 END) AS chargeback_amount
FROM combined
GROUP BY TO_CHAR(trans_date, 'YYYY-MM'), country
HAVING SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) > 0 
OR SUM(CASE WHEN state = 'chargeback' THEN amount ELSE 0 END) > 0
ORDER BY TO_CHAR(trans_date, 'YYYY-MM');
