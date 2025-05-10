
import sqlite3
import pandas as pd

# Crear la base de datos y conexión
db_path = "base/viajes.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Crear la tabla 'viajes'
cursor.execute("""
CREATE TABLE IF NOT EXISTS viajes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_persona INTEGER NOT NULL,
    destino TEXT NOT NULL,
    origen TEXT NOT NULL,
    valor REAL NOT NULL,
    dias_viaje INTEGER NOT NULL
);
""")


# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()
