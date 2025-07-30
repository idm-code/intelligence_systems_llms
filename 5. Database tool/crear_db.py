import sqlite3

conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Crear tabla de usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
)
""")

# Insertar algunos usuarios de ejemplo
cursor.executemany(
    "INSERT INTO usuarios (nombre) VALUES (?)",
    [("Ana",), ("Luis",), ("Marta",), ("Pedro",)]
)

conn.commit()
conn.close()
print("Base de datos creada y poblada con éxito.")