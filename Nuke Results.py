import sqlite3

# Connect to the database
conn = sqlite3.connect("cities.db")
cursor = conn.cursor()

# Execute a DELETE query to remove all rows from the table
cursor.execute("DELETE FROM selected_cities")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
