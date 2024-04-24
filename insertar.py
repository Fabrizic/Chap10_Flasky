import sqlite3
from datetime import datetime, timezone

# Crear un adaptador de fecha y hora
def adapt_datetime(dt):
    return dt.strftime('%Y-%m-%d %H:%M:%S')

# Registrar el adaptador
sqlite3.register_adapter(datetime, adapt_datetime)

# Crear un convertidor de fecha y hora
def convert_datetime(s):
    return datetime.strptime(s.decode('utf-8'), '%Y-%m-%d %H:%M:%S')

# Registrar el convertidor
sqlite3.register_converter('datetime', convert_datetime)

def insert_data(database):
    conn = sqlite3.connect(database, detect_types=sqlite3.PARSE_DECLTYPES)
    c = conn.cursor()

    # Borrar los registros existentes
    c.execute('DELETE FROM roles')
    c.execute('DELETE FROM users')

    # Insertar datos en la tabla roles
    roles = [
        (1, 'Admin', 1, 0xFF),
        (2, 'User', 0, 0x01),
    ]
    c.executemany('''
        INSERT INTO roles (id, name, "default", permissions)
        VALUES (?, ?, ?, ?)
    ''', roles)

    # Insertar datos en la tabla users
    users = [
        (1, 'admin@example.com', 'admin', 1, 'password_hash', 1, 'Admin', 'Location', 'About me', datetime.now(timezone.utc), datetime.now(timezone.utc), 'avatar_hash'),
        (2, 'user@example.com', 'user', 2, 'password_hash', 0, 'User', 'Location', 'About me', datetime.now(timezone.utc), datetime.now(timezone.utc), 'avatar_hash'),
    ]
    c.executemany('''
        INSERT INTO users (id, email, username, role_id, password_hash, confirmed, name, location, about_me, member_since, last_seen, avatar_hash)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', users)

    conn.commit()
    conn.close()

if __name__ == '__main__':
    insert_data('data.sqlite')
    insert_data('data-dev.sqlite')