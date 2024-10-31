-- Question 1: First 14-Day Satisfaction
-- create
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    signup_timestamp timestamp
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    trip_id INT,
    status VARCHAR(50),
    order_timestamp timestamp,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE trips (
    dasher_id INT,
    trip_id INT PRIMARY KEY,
    estimated_delivery_timestamp timestamp,
    actual_delivery_timestamp timestamp
);


-- Insert data into customers table
INSERT INTO customers (customer_id, signup_timestamp) VALUES
(8472, '2022-05-30 00:00:00'),
(2341, '2022-06-01 00:00:00'),
(1314, '2022-06-03 00:00:00'),
(1435, '2022-06-05 00:00:00'),
(5421, '2022-06-07 00:00:00');

-- Insert data into orders table
INSERT INTO orders (order_id, customer_id, trip_id, status, order_timestamp) VALUES
(727424, 8472, 100463, 'completed successfully', '2022-06-05 09:12:00'),
(242513, 2341, 100482, 'completed incorrectly', '2022-06-05 14:40:00'),
(141367, 1314, 100362, 'completed incorrectly', '2022-06-07 15:03:00'),
(582193, 5421, 100657, 'never_received', '2022-07-07 15:22:00'),
(253613, 1314, 100213, 'completed successfully', '2022-06-12 13:43:00');

-- Insert data into trips table
INSERT INTO trips (dasher_id, trip_id, estimated_delivery_timestamp, actual_delivery_timestamp) VALUES
(101, 100463, '2022-06-05 09:42:00', '2022-06-05 09:38:00'),
(102, 100482, '2022-06-05 15:10:00', '2022-06-05 15:46:00'),
(101, 100362, '2022-06-07 15:33:00', '2022-06-07 16:45:00'),
(102, 100657, '2022-07-07 15:52:00', NULL),
(103, 100213, '2022-06-12 14:13:00', '2022-06-12 14:10:00');


-- These issues include:

-- Orders being completed incorrectly, with missing items or wrong orders.
-- Orders not being received due to incorrect addresses or drop-off spots.
-- Orders being delivered late, with the actual delivery time being 30 minutes later than the order placement time. 
-- Note that the estimated_delivery_timestamp is automatically set to 30 minutes after the order_timestamp.
-- Write a query that calculates the bad experience rate for new users who signed up in June 2022 during their first 14 days on the platform. The output should include the percentage of bad experiences, rounded to 2 decimal places.

-- fetch 
select * from customers;
select * from orders;
select * from trips;

WITH new_user_june_2022 AS (
    SELECT *
    FROM customers
    WHERE signup_timestamp BETWEEN '2022-06-01' AND '2022-06-30'
),

base_table AS (
    SELECT 
        users.customer_id,
        users.signup_timestamp,
        o.order_id,
        o.status,
        o.order_timestamp,
        t.estimated_delivery_timestamp,
        t.actual_delivery_timestamp
    FROM new_user_june_2022 AS users
    LEFT JOIN orders AS o ON users.customer_id = o.customer_id
    LEFT JOIN trips AS t ON t.trip_id = o.trip_id
    WHERE o.order_id IS NOT NULL 
      AND o.order_timestamp BETWEEN users.signup_timestamp 
      AND users.signup_timestamp + INTERVAL '14 days'
)

SELECT 
    ROUND(
        100.0 * COUNT(CASE 
            WHEN bt.status IN ('completed incorrectly', 'never_received') 
              OR bt.actual_delivery_timestamp > bt.estimated_delivery_timestamp 
            THEN 1 
            ELSE NULL 
        END) / COUNT(*), 2
    ) AS bad_experience_pct
FROM base_table AS bt
INNER JOIN new_user_june_2022 AS users ON users.customer_id = bt.customer_id;
