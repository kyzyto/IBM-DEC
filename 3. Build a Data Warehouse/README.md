### Primary Tools / Software
- ERD Design Tool of ```pgAdmin```
- <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white"> ```Database Server```

#### Scenario
As a data engineer hired by an ecommerce company named SoftCart.com . The company retails download only items like E-Books, Movies, Songs etc. The company has international presence and customers from all over the world. The company would like to create a data warehouse so that it can create reports like;

* total sales per year per country
* total sales per month per category
* total sales per quarter per country
* total sales per category per country
Utilize data warehousing skills to design and implement a data warehouse for the company.


#### Objective
- Design a Data Warehouse using the pgAdmin ERD design tool.
- Create the schema in the Data Warehouse

### Data Warehousing
#### Requirements:
- Created and instance of IBM DB2 on the cloud
- Design a data warehouse.
- Use e-commerce company sample data
- Design a Star Schema for the warehouse
- Identify the columns for the various dimension and fact tables in the schema.
- Name the database **softcart** and then use the ERD design tool to design the table **softcartDimDate** using fields such as DateID, Month, Monthname, and so on.
- Goal of company is that company would like to have the ability to generate the report on a yearly, monthly, daily, and weekday basis.
- Designed the dimension tables **softcartDimCategory, softcartDimCountry** and **softcartFactSales** using ERD design tool.
- Design the required relationships (one-to-one, one-to-many, and so on) amongst the tables.
- load the data into the data warehouse
- Senior Data Engineer reviews design and make improvements to your schema design.
- Download the data as per the improved schema and restore it into a database named staging using the pgAdmin.

### Data Warehousing Reporting
#### Requirements:
- Load the data provided by the company into the tables in CSV format by performing a series of tasks.
- Download the data from the links provided and then load that data into the DimDate table, DimCategory table, DimCountry table, and fact table FactSales.
- Query the loaded data by creating a grouping sets query, rollup query, and cube query using the columns **Orderid, Category,** and **Price collected.**
- Create an MQT(Materialized Query Table) named Total_sales_per_country using the country and total sales columns.
