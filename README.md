## MonogDB To MySQL Database Converter

This converter gets the JSON data from the given link and convert that JSON data to the MySQL Database in the localhost.

# Prerequisites
1. MySQL
2. Python3
3. PyMySQL

# How to run
1. Input the MySQL credentials in the **config.ini** file.
2. Run **json_to_mysql.py** and input the name of the database you want to use or create the database.

# How it works
1. **get_data.py**

	Get the json format data from the given link in the code. You can enter the link in the **get_data.py**.

2. **create_mysql_tables.py**

	This file contains different funciton which execute the different SQL queries (like creating database, tables and insert of data). Generally, this is the utility file which is used by **json_to_mysql.py**

3. **json_to_mysql.py**

	This is the main/driver file. This file recives the json format data from **get_data.py** and then save that data into MySQL database.

4. **python_mysql_dbconfig.py**

	This script file reads the __config.ini__ which contains the information required for the connection to the MySQL server.
	
