### Primary Tools / Software
- <img src="https://img.shields.io/badge/mysql-%2300f.svg?style=for-the-badge&logo=mysql&logoColor=white">
- <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54">
- <img src="https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=Apache%20Airflow&logoColor=white">
- <img src="https://img.shields.io/badge/shell_script-%23121011.svg?style=for-the-badge&logo=gnu-bash&logoColor=white"></p>

#### Objective
ETL and Data Pipelines using Apache AirFlow

#### ETL and Data Pipeline using Apache Airflow requirement:
***ETL*** <br>

- Phase 1
  - Prepared `MySQL Server` and `MongoDB Server`
  - Downloaded the files database from source
  - Imported data in JSON file to database and collection in MongoDB server
  - Imported data in SQL file to the MySQL server
  - Extracted data from tables in MySQL and from the MongoDB databases to into CSV format
- Phase 2
  - Transformed the `OLTP` data to suit the data warehouse schema
  - Read the OLTP data in the CSV format
  - Added, Edited, and Dropped columns based on the data warehouse schema 
  - Then saved the transformed data into a new CSV file.
- Phase 3
  -  Performed a series of tasks to transform the data 
  -  Loaded the transformed data into the data warehouse 
  -  Read the transformed data in the CSV format
  -  Loaded the transformed data into the data warehouse
  -  Then verified that the data is loaded properly
- Phase 4
  - Automated the extraction of daily incremental data
  - Loaded yesterday's data into the data warehouse. 
  - Use python script to automatically loads yesterday's data from the production database into the data warehouse.

***Apache AirFlow***<br>

- Prepared `Apache AirFlow Serever`
- Downloaded the dataset from the source
- Performed a series of tasks to create a `DAG` that runs daily.
- Create a task that extracts the IP address field from the webserver log file and then saves it into a text file
- Create a task that filters out all the occurrences of IP address "xxx.xxx.xxx" from text file and save the output to a new text file
- Loaded the data by archiving the transformed text file into a TAR file.
- Defined the the task pipeline as per the given details
- Got the DAG operational by saving the defined DAG into a PY file.
- Unpause and then monitor the DAG runs for the Airflow console
