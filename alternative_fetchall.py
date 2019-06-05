# Fetchall is dangerous
#   fecthall can depleat our instant memory if there is too much data
#   Bringing our servers to a halt - like having too many tabs

# We can use a while lopp fetching one at a time
#   be aware of query optimization for external DB services and hosted DBs
#   these usually charge per call on th db
import csv
from connection_db import *


rows = cursor.execute("SELECT * FROM Customers WHERE City = 'London' "
                      "AND (ContactName LIKE '%m%' OR ContactName LIKE '%n%')")
new_data = []
while True:
    record = rows.fetchone()
    if record is None:
        break
    new_data.append([record.ContactName])

print(new_data)

new_file = open("n_and_m_london_customers.csv", 'w', newline='')

#write to that file
with new_file:
    csv_writer = csv.writer(new_file)
    csv_writer.writerows(new_data)
