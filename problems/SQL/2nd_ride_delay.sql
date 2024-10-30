-- Uber SQL Question 2: 2nd Ride Delay 
-- Create users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    registration_date DATE
);

-- Create rides table
CREATE TABLE rides (
    ride_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(user_id),
    ride_date DATE
);

-- Insert data into users table
INSERT INTO users (user_id, registration_date) VALUES
(1, '2022-08-15'),
(2, '2022-08-21');

-- Insert data into rides table
INSERT INTO rides (ride_id, user_id, ride_date) VALUES
(1, 1, '2022-08-15'),
(2, 1, '2022-08-16'),
(3, 2, '2022-09-20'),
(4, 2, '2022-09-23');


-- As a data analyst at Uber, it's your job to report the latest metrics for specific groups of Uber users. 
-- Some riders create their Uber account the same day they book their first ride; the rider engagement team calls them "in-the-moment" users.

-- Uber wants to know the average delay between the day of user sign-up and the day of their 2nd ride. 
-- Write a query to pull the average 2nd ride delay for "in-the-moment" Uber users. Round the answer to 2-decimal places.

-- fetch 
select * from rides;
select * from users;


WITH in_moment_users AS (
    SELECT
        u.user_id,
        u.registration_date
    FROM 
        users AS u
    LEFT JOIN 
        rides AS r ON u.user_id = r.user_id
    WHERE 
        r.ride_date = u.registration_date
),

ride_number AS (
    SELECT
        user_id,
        ride_date,
        ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY ride_date ASC) AS row_num
    FROM 
        rides
)

SELECT 
    ROUND(AVG(EXTRACT(DAY FROM AGE(rn.ride_date, imu.registration_date))), 2) AS average_delay
FROM 
    in_moment_users AS imu 
LEFT JOIN 
    ride_number AS rn ON imu.user_id = rn.user_id
WHERE 
    rn.row_num = 2;


