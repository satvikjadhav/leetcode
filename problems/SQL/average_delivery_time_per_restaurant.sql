-- Question 6: Average Delivery Time per Restaurant
-- Create the orders table
CREATE TABLE orders (
    order_id VARCHAR(10) PRIMARY KEY,
    order_time timestamp,
    delivery_time timestamp,
    restaurant_id INT,
    customer_id INT
);

-- Insert values into the orders table
INSERT INTO orders (order_id, order_time, delivery_time, restaurant_id, customer_id) VALUES
('0001', '2021-08-25 18:00:00', '2021-08-25 18:40:00', 100, 123),
('0002', '2021-08-25 19:00:00', '2021-08-25 19:30:00', 200, 265),
('0003', '2021-08-25 20:00:00', '2021-08-25 20:40:00', 200, 362),
('0004', '2021-08-25 21:00:00', '2021-08-25 21:35:00', 300, 192),
('0005', '2021-08-25 22:00:00', '2021-08-25 22:45:00', 100, 981);


-- Assume that we calculate the delivery time by the difference between the order time and delivery completion time. 
-- Can you write a SQL query to find the average delivery time for each restaurant?

-- from: https://datalemur.com/blog/doordash-sql-interview-questions

-- fetch 
SELECT 
    restaurant_id,
    ROUND(AVG(EXTRACT(EPOCH FROM (delivery_time - order_time)) / 60), 1) AS avg_delivery_time_in_minutes
FROM 
    orders
GROUP BY 
    restaurant_id
ORDER BY 
    restaurant_id;



