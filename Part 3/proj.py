 import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """
    Creates a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    """
    Creates a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def main():
    database = r"store.db"

    sql_create_categories_table = """CREATE TABLE IF NOT EXISTS categories (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL);"""

    sql_create_products_table = """CREATE TABLE IF NOT EXISTS products (
                                id integer PRIMARY KEY,
                                name text NOT NULL,
                                price real NOT NULL,
                                description text NOT NULL,
                                category_id integer NOT NULL,
                                FOREIGN KEY (category_id) REFERENCES categories (id));"""

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create categories table
        create_table(conn, sql_create_categories_table)
        # create products table
        create_table(conn, sql_create_products_table)
    else:
        print("Error! cannot create the database connection.")

    # close database connection
    if conn:
        conn.close()

if __name__ == '__main__':
    main()
