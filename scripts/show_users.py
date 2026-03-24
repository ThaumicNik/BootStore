import sqlite3


conn = sqlite3.connect("app.db")
conn.row_factory = sqlite3.Row
rows = conn.execute(
    """
    SELECT u.full_name, u.email, u.password, r.role_name
    FROM users u
    JOIN roles r ON r.id = u.role_id
    ORDER BY r.id, u.id
    """
).fetchall()

for row in rows:
    print(f"{row['role_name']} | {row['email']} | {row['password']} | {row['full_name']}")
