# Import libraries required for connecting to mysql

# Import libraries required for connecting to DB2

# Connect to MySQL
import mysql.connector

# connect to database
connection = mysql.connector.connect(user='root', password='ODAwOS1yYW1lc2hz',host='127.0.0.1',database='sales')

# create cursor

cursor = connection.cursor()
# Connect to DB2

# Find out the last rowid from DB2 data warehouse
# The function get_last_rowid must return the last rowid of the table sales_data on the IBM DB2 database.

def get_last_rowid():
	SQL = "SELECT MAX(ROWID) FROM sales_data"
	stmnt = ibm_db.exec_immediate(conn, SQL)
	tuple = ibm_db.fetch_tuple(stmt)
	return(tuple[0])


last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# List out all records in MySQL database with rowid greater than the one on the Data warehouse
# The function get_latest_records must return a list of all records that have a rowid greater than the last_row_id in the sales_data table in the sales database on the MySQL staging data warehouse.

def get_latest_records(rowid):
	SQL = "SELECT * FROM sales_data WHERE rowid > " + str(rowid)
	cursor.execute(SQL)
	result_set = cursor.fetchall()
	return(result_set)


new_records = get_latest_records(last_row_id)

print("New rows on staging datawarehouse = ", len(new_records))

# Insert the additional records from MySQL into DB2 data warehouse.
# The function insert_records must insert all the records passed to it into the sales_data table in IBM DB2 database.

def insert_records(records):
	SQL = "INSERT INTO sales_data(rowid, product_id, customer_id, quantity) VALUES(?,?,?,?);"
	stmt = ibm_db.prepare(conn, SQL)
	for row in records:
		row1 = (row[0], row[1], row[1], row[2], row[3])
		ibm_db.execute(stmt, row1)

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# disconnect from mysql warehouse

# disconnect from DB2 data warehouse

# End of program