from sqlite3 import Connection, connect
from garden_api import types_pb2 as garden_messages
from typing import Optional, Iterable

GARDEN_DB_NAME = "garden.db"


class ValidationError(Exception):
    pass


def get_conn() -> Connection:
    conn = connect(GARDEN_DB_NAME)

    create_tables_if_needed(conn)

    return conn


def create_tables_if_needed(conn: Connection) -> None:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS gardens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            place TEXT NOT NULL,
            name TEXT NOT NULL
        );
    """)


def get_gardens(conn: Connection, name: Optional[str] = None) -> Iterable[garden_messages.Garden]:
    cur = conn.execute("SELECT * FROM gardens")

    for row in cur:
        row_garden_id, row_place, row_name = row

        if name is not None and row_name != name:
            continue
        
        yield garden_messages.Garden(name=row_name, place=row_place, garden_id=row_garden_id)
    

def create_garden(conn: Connection, name: str, place: str) -> garden_messages.Garden:
    if len(list(get_gardens(conn, name=name))) != 0:
        raise ValidationError("This name already exists")
    
    cur = conn.cursor()
    
    cur.execute("""
        INSERT INTO gardens (place, name) 
        VALUES (?, ?);
    """, (place, name))

    conn.commit()

    return list(get_gardens(conn, name=name))[-1]

    