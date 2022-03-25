### Primary Tools / Software
- <img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white">
- ```phpMyAdmin```

#### Objective
- Designed schema for OLTP database by storing data like row ID, product ID, customer ID, price, quantity, and time stamp of sale.
- Loaded the data into the OLP database.
- Performed some advanced querying.
- Automated admin tasks by writing a query to list all the records created in the last 24 hours and thenn export them to a file.
- Wrote shell/bash script that exports records created in the last 24 hours into another file.


#### OLTP databse:
OLTP database in generally used to handle every day business transactions of an organization like a bank or a super market chain. OLTP databases can be write heavy or may have a balance read/write load.

#### OLTP database requirements:
- Handles huge number of transactions per second.
- Transactions involve accessing(i.e read/write to) a minute portion of the database.
- Payload per transaction is small.
- Latency(i.e *time taken to execute a transaction*) needs to be very less. 

#### OLTP database design:
- Highly normalized schema so as to achieve a very low latency.
- Stored only the recent data like the last few week's data, hence further improving the latency an OLTP database.
- Ran on storage that is very fast like SSD due to requirements. 
