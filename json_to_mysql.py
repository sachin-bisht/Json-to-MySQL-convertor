import get_data as gd
import create_mysql_tables as cmt


table1 = {}
column1 = ''
new_tables = {}
keys = ''
values = ''
new_table = {}

mcolumn = []
mvalues = []

def mdict(mydict, name, c = 0):

	global table1
	global column1
	global new_tables
	global keys
	global values
	global new_table
	
	global mcolumn
	global mvalues

	for key, value in mydict.items():
		if type(value) is str or type(value) is int or type(value) is bool or type(value) is float:
			table1[name+'_'+str(key)] = value
			
			temp = []
			for ij in str(key):
				if ij == '-':
					temp.append('_')
				else:
					temp.append(ij)
			key = ''.join(temp)

			mcolumn.append(name + '_' + str(key))
			mvalues.append(value)

			column1 += name + '_' + str(key) + ' '
			keys += name + '_' + str(key) + ', '

			if type(value) is str:
				values += '"' + str(value) + '", '
				column1 += 'varchar(500), '
			elif type(value) is int:
				values += str(value) + ', '
				column1 += 'int(18), '
			elif type(value) is float:
				values += str(value) + ', '
				column1 += 'decimal(19, 6), '
			else:
				values += str(value) + ', '
				column1 += 'boolean, '

		elif type(value) is dict:
			nname = name+'_'+str(key)
			mdict(value, nname, c)
		else:
			if c == 0:
				new_tables[key] = value
			else:
				new_table[key] = value

def create_table_query(database, data):
	global table1
	global column1
	global new_tables
	global keys
	global values
	global new_table

	global mcolumn
	global mvalues

	i = 0

	file = open('text.sql', 'w')

	for key,value in data.items():
		if type(value) is str or type(value) is int or type(value) is bool or type(value) is float:
			table1[key] = value

			temp = []
			for ij in str(key):
				if ij == '-':
					temp.append('_')
				else:
					temp.append(ij)
			key = ''.join(temp)

			mcolumn.append(str(key))
			mvalues.append(value)

			column1 += str(key) + ' '
			keys += str(key) + ', '

			if type(value) is str:
				values += '"' + str(value) + '", '
				column1 += 'varchar(100), '
			elif type(value) is int:
				values += str(value) + ', '
				column1 += 'int(18), '
			elif type(value) is float:
				values += str(value) + ', '
				column1 += 'decimal(19, 6), '
			else:
				values += str(value) + ', '
				column1 += 'boolean, '

		elif type(value) is dict:
			name = str(key)
			mdict(value, name)
		else:
			new_tables[key] = value

	tablename = 'table{}'.format(i)
	i += 1

	if len(column1) > 2:
		column1 = column1[:-2]

	query = "create table {}({})".format(tablename, column1)

	file.write(query)
	file.write('\n\n\n')

	cmt.execute_query(database, query)
	
	if len(keys) > 1:
		keys = keys[:-2]
	if len(values) > 1:
		values = values[:-2]

	cmt.insert_remaining_columns(database,tablename, mcolumn, mvalues)

	query = "insert into {} ({}) values ({})".format(tablename, keys, values)
	file.write(query)
	file.write('\n\n\n')

	cmt.execute_query(database, query, tt=1)

	while True:
		for key, value in new_tables.items():
			mmm = 0
			for val in value:
				table1 = {}
				column1 = ''
				keys = ''
				values = ''
				new_table = {}
				mcolumn = []
				mvalues = []

				if type(val) is str or type(val) is int or type(val) is bool or type(val) is float:
					table1[key] = val

					temp = []
					for ij in str(key):
						if ij == '-':
							temp.append('_')
						else:
							temp.append(ij)
					key = ''.join(temp)

					mcolumn.append(str(key))
					mvalues.append(value)

					column1 += str(key) + ' '
					keys += str(key) + ', '
					
					if type(val) is str:
						values += '"' + str(val) + '", '
						column1 += 'varchar(100), '
					elif type(val) is int:
						values += str(val) + ', '
						column1 += 'int(18), '
					elif type(val) is float:
						values += str(val) + ', '
						column1 += 'decimal(19, 6), '
					else:
						values += str(val) + ', '
						column1 += 'boolean, '

				elif type(val) is dict:
					name = str(key)
					mdict(val, name, c = 1)
				else:
					new_table[key] = val

				if len(column1) > 2:
					column1 = column1[:-2]
				if mmm == 0:
					tablename = 'table{}_{}'.format(i, str(key))
					i += 1
					query = "create table {}({})".format(tablename, column1)
					file.write(query)
					file.write('\n\n\n')
					cmt.execute_query(database, query)
					mmm = 1
				
				cmt.insert_remaining_columns(database, tablename, mcolumn, mvalues)

				if len(keys) > 1:
					keys = keys[:-2]
				if len(values) > 1:
					values = values[:-2]
				


				query = "insert into {} ({}) values ({})".format(tablename, keys, values)
				file.write(query)
				file.write('\n\n\n')

				cmt.execute_query(database, query, tt=1)

		if not new_table:
			break
		else:
			new_tables = new_table




def proc():
	data = gd.get_data()
	database = cmt.create_database()
	create_table_query(database, data)

proc()