CREATE DATABASE sales;

USE sales;

CREATE TABLE sales_data ( product_id INT PRIMARY KEY NOT NULL, customer_id INT NOT NULL, price INT NOT  NULL, quantity INT  NOT NULL, timestamp TIMESTAMP NOT NULL);

INSERT INTO sales_data (product_id, customer_id, price, quantity, timestamp) 
VALUES (6739, 76305, 230, 1, '2020-09-05 16:20:03'),
(7460, 81008, 1455, 4, '2020-09-05 16:20:04'),
(6701, 7556, 1159, 2, '2020-09-05 16:20:05'),
(8021, 36492, 3727, 2, '2020-09-05 16:20:06'),
(6442, 11282, 4387, 5, '2020-09-05 16:20:07');

SELECT * FROM sales_data ORDER BY timestamp ASC;