-- Question 4: Restaurant Performance Analysis
-- Create the restaurants table
CREATE TABLE restaurants (
    restaurant_id VARCHAR(10) PRIMARY KEY,
    restaurant_name VARCHAR(100)
);

-- Insert values into the restaurants table
INSERT INTO restaurants (restaurant_id, restaurant_name) VALUES
('001', 'Burger King'),
('002', 'KFC'),
('003', 'McDonald'),
('004', 'Pizza Hut'),
('005', 'Starbucks');

-- Create the users table
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(100)
);

-- Insert values into the users table
INSERT INTO users (user_id, user_name) VALUES
(101, 'John Doe'),
(102, 'Jane Smith'),
(103, 'Bob Johnson'),
(104, 'Alice Anderson'),
(105, 'Emma Wilson');

-- Create the orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    user_id INT,
    restaurant_id VARCHAR(10),
    order_date DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (restaurant_id) REFERENCES restaurants(restaurant_id)
);

-- Insert values into the orders table
INSERT INTO orders (order_id, user_id, restaurant_id, order_date) VALUES
(2001, 101, '001', '2022-10-01'),
(2002, 102, '002', '2022-10-02'),
(2003, 101, '003', '2022-10-03'),
(2004, 103, '002', '2022-10-04'),
(2005, 102, '001', '2022-10-05'),
(2006, 104, '004', '2022-10-06'),
(2007, 105, '005', '2022-10-07'),
(2008, 101, '001', '2022-10-08'),
(2009, 102, '002', '2022-10-09'),
(2010, 104, '005', '2022-10-10');

-- As a DoorDash data analyst, your task is to understand the behavior and preferences of DoorDash users, 
-- which would be fundamental in improving the service. One of the essential measures of service quality 
-- and restaurant popularity is the number of orders each restaurant receives over time. 

-- Your task is to design a database consisting of restaurants, users, and orders.

-- Given the restaurants, users, and orders tables below, 
-- please write a query to identify the top 5 restaurants with the most orders in the last month.

-- fetch 
select * from restaurants;
select * from users;
select * from orders;


SELECT 
    r.restaurant_name, 
    COUNT(o.order_id) AS count_orders
FROM 
    orders AS o
LEFT JOIN 
    restaurants AS r ON o.restaurant_id = r.restaurant_id 
WHERE 
    order_date >= NOW() - INTERVAL '1 month'
GROUP BY 
    r.restaurant_name
ORDER BY 
    count_orders DESC
LIMIT 5;
