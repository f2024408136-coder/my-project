import sqlite3


# Database connect
con = sqlite3.connect("project.db")

# Cursor object
cursor = con.cursor()


# Create table query
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")


print("Table created successfully!")


# Save changes
con.commit()

# Close connection
con.close()