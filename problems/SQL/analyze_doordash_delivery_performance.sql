-- Create the deliveries table
CREATE TABLE deliveries (
    delivery_id INT PRIMARY KEY,
    driver_id INT,
    delivery_start_time timestamp,
    delivery_end_time timestamp
);

-- Insert values into the deliveries table
INSERT INTO deliveries (delivery_id, driver_id, delivery_start_time, delivery_end_time) VALUES
(1, 123, '2022-08-01 14:00:00', '2022-08-01 14:40:00'),
(2, 123, '2022-08-01 15:15:00', '2022-08-01 16:10:00'),
(3, 265, '2022-08-01 14:00:00', '2022-08-01 15:30:00'),
(4, 265, '2022-08-01 16:00:00', '2022-08-01 16:50:00'),
(5, 123, '2022-08-02 11:00:00', '2022-08-02 11:35:00');


-- The output should have the following fields:
--     -driver_id
--     -day
--     -avg_delivery_duration: Average minutes taken to for a delivery in a particular day
--     -rank: Rank over the daily average duration for each driver
--     -overall_avg_delivery_duration: Average minutes taken to deliver for all deliveries the driver has made
-- from: https://datalemur.com/blog/doordash-sql-interview-questions

-- fetch 
select * from deliveries;

WITH avg_delivery_by_date AS (
    SELECT
        driver_id,
        DATE(delivery_start_time) AS delivery_date,
        AVG(EXTRACT(EPOCH FROM (delivery_end_time - delivery_start_time)) / 60) 
            OVER (PARTITION BY driver_id, DATE(delivery_start_time)) AS avg_time_taken_to_deliver
    FROM 
        deliveries
)

SELECT
    driver_id,
    delivery_date,
    avg_time_taken_to_deliver AS avg_delivery_duration,
    RANK() OVER (PARTITION BY driver_id ORDER BY avg_time_taken_to_deliver ASC) AS rank,
    AVG(avg_time_taken_to_deliver) OVER (PARTITION BY driver_id) AS overall_avg_delivery_duration
FROM 
    avg_delivery_by_date;

