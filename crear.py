import sqlite3

def create_table(database):
    conn = sqlite3.connect(database)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE roles (
            id INTEGER PRIMARY KEY,
            name TEXT UNIQUE NOT NULL,
            "default" BOOLEAN NOT NULL DEFAULT 0,
            permissions INTEGER,
            users TEXT
        )
    ''')

    c.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            email TEXT UNIQUE NOT NULL,
            username TEXT UNIQUE NOT NULL,
            role_id INTEGER,
            password_hash TEXT,
            confirmed BOOLEAN NOT NULL DEFAULT 0,
            name TEXT,
            location TEXT,
            about_me TEXT,
            member_since DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_seen DATETIME DEFAULT CURRENT_TIMESTAMP,
            avatar_hash TEXT,
            FOREIGN KEY(role_id) REFERENCES roles(id)
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table('data.sqlite')
    create_table('data-dev.sqlite')