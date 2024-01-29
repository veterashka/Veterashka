import sqlite3
conn = sqlite3.connect('Zad_two.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS Tab_1(col_1 TEXT, col_2 TEXT, col_3 TEXT)''')
cursor.execute('''INSERT INTO Tab_1(col_1, col_2, col_3) VALUES ('wan', 'two:', '"three"')''')
conn.commit()