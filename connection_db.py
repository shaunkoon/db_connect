import pyodbc

# # Our variable to create a connection
server = 'localhost,1433'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

# # Making a connection
docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# # Creating a cursor that can execute SQL functions on connected db
cursor = docker_Northwind.cursor()

# Maintains State
cursor.execute("SELECT * FROM Customers WHERE Fax IS NULL ")

# Fetchone method
# row = cursor.fetchone()
# print(row)
# print(row.CompanyName)

# fetchall method
rows_all = cursor.fetchall()
#print(len(rows_all))

# for rows in rows_all:
#     print('Company Name:', row.CompanyName)
#     print('Fax:' , row.Fax)
#     print("Contact Name:", row.ContactName)
#     print("-")

# for row in rows_all:
#     print('Company Name:', row.CompanyName)
#     print('Phone:', row.Phone)
#     print("Contact Name:", row.ContactName)
#     print("Fax:", row.Fax)
#     print("-")





