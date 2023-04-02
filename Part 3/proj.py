def create_connection(db_file):      #https://www.sqlitetutorial.net/sqlite-python/creating-tables/
    """ create a database connection to the SQLite database
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




if __name__ == '__main__':
    main()
