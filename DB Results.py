import sqlite3

# Connect to the database
conn = sqlite3.connect("cities.db")
cursor = conn.cursor()

# Execute a SELECT query to retrieve all rows from the table
cursor.execute("SELECT * FROM selected_cities")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Print the contents of the table
for row in rows:
    print(row)

# Close the connection
conn.close()
