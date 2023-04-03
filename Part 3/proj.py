#NEW VERSION
import sqlite3
from sqlite3 import Error
import sys


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
        print (e)

    return conn

def create_table(conn, create_table_sql):
    """
    Creates a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    c.execute(create_table_sql)

def main():
    database = r"ABCFull.db"

    sql_create_Video_table = """CREATE TABLE IF NOT EXISTS Video (
                                videoCode integer PRIMARY KEY,
                                videoLength INTEGER);"""

    sql_create_Model_table = """CREATE TABLE IF NOT EXISTS Model (
                                    modelNo CHAR(10) PRIMARY KEY,
                                    width NUMERIC(6,2),
                                    height NUMERIC(6,2),
                                    weight NUMERIC(6,2),
                                    depth NUMERIC(6,2),
                                    screenSize NUMERIC(6,2));"""

    sql_create_Site_table = """CREATE TABLE IF NOT EXISTS Site ( 
                                    siteCode INTEGER PRIMARY KEY,
                                    type VARCHAR(16),
                                    addr VARCHAR(50),
                                    phone VARCHAR(16),
                                    CHECK (type IN ('bar', 'restaurant')));"""

    sql_create_DigitalDisplay_table = """CREATE TABLE IF NOT EXISTS DigitalDisplay ( 
                                    serialNo CHAR(10) PRIMARY KEY,
                                    schedulerSystem CHAR(10) CHECK (schedulerSystem IN ('Random', 'Smart', 'Virtue')),
                                    modelNo CHAR(10),
                                    FOREIGN KEY (modelNo) REFERENCES Model (modelNo));"""

    sql_create_Client_table = """CREATE TABLE IF NOT EXISTS Client (
                                    clientId INTEGER PRIMARY KEY,
                                    name VARCHAR(40),
                                    phone VARCHAR(16),
                                    addr VARCHAR(50));"""

    sql_create_TechnicalSupport_table = """CREATE TABLE IF NOT EXISTS TechnicalSupport (
                                    empId INTEGER PRIMARY KEY,
                                    name VARCHAR(40),
                                    gender CHAR(1));"""

    sql_create_Administrator_table = """CREATE TABLE IF NOT EXISTS Administrator (
                                    empId INTEGER PRIMARY KEY,
                                    name VARCHAR(40),
                                    gender CHAR(1));"""

    sql_create_Salesman_table = """CREATE TABLE IF NOT EXISTS Salesman (
                                        empId INTEGER PRIMARY KEY,
                                        name VARCHAR(40),
                                        gender CHAR(1));"""

    sql_create_AirtimePackage_table = """CREATE TABLE IF NOT EXISTS AirtimePackage (
                                            packageId INTEGER PRIMARY KEY,
                                            class VARCHAR(16) CHECK (class IN ('economy', 'whole day', 'golden hours')),
                                            startDate DATE,
                                            lastDate DATE,
                                            frequency INTEGER,
                                            videoCode INTEGER,
                                            FOREIGN KEY (videoCode) REFERENCES Video (videoCode));"""

    sql_create_AdmWorkHours_table = """CREATE TABLE IF NOT EXISTS AdmWorkHours (
                                            empId INTEGER,
                                            day DATE,
                                            hours NUMERIC(4,2),
                                            PRIMARY KEY (empId, day),
                                            FOREIGN KEY (empId) REFERENCES Administrator (empId));"""

    sql_create_Broadcasts_table = """CREATE TABLE IF NOT EXISTS Broadcasts (
                                                videoCode INTEGER,
                                                siteCode INTEGER,
                                                PRIMARY KEY (videoCode, siteCode),
                                                FOREIGN KEY (videoCode) REFERENCES Video (videoCode),
                                                FOREIGN KEY (siteCode) REFERENCES Site (siteCode));"""

    sql_create_Administers_table = """CREATE TABLE IF NOT EXISTS Administers (
                                            empId INTEGER,
                                            siteCode INTEGER,
                                            PRIMARY KEY (empId, siteCode),
                                            FOREIGN KEY (empId) REFERENCES Administrator (empId),
                                            FOREIGN KEY (siteCode) REFERENCES Site (siteCode));"""

    sql_create_Specializes_table = """CREATE TABLE IF NOT EXISTS Specializes (
                                                empId INTEGER,
                                                modelNo CHAR(10),
                                                PRIMARY KEY (empId, modelNo),
                                                FOREIGN KEY (empId) REFERENCES TechnicalSupport (empId),
                                                FOREIGN KEY (modelNo) REFERENCES Model (modelNo));"""

    sql_create_Purchases_table = """CREATE TABLE IF NOT EXISTS Purchases (
                                                    clientId INTEGER,
                                                    empId INTEGER,
                                                    packageId INTEGER,
                                                    commissionRate NUMERIC(4,2),
                                                    PRIMARY KEY (clientId, empId, packageId),
                                                    FOREIGN KEY (clientId) REFERENCES Client (clientId),
                                                    FOREIGN KEY (empId) REFERENCES Salesman (empId),
                                                    FOREIGN KEY (packageId) REFERENCES AirtimePackage (packageId));"""

    sql_create_Locates_table = """CREATE TABLE IF NOT EXISTS Locates (
                                                    serialNo CHAR(10),
                                                    siteCode INTEGER,
                                                    PRIMARY KEY (serialNo, siteCode),
                                                    FOREIGN KEY (serialNo) REFERENCES DigitalDisplay (serialNo),
                                                    FOREIGN KEY (siteCode) REFERENCES Site (siteCode));"""


def query_one(db_file, street_name):

    conn = creat_connection(db_file)
    
    cur = conn.cursor()
    cur.execute('Select * FROM Site WHERE address LIKE ?',('%{}%'.format(street_name),))
    
    rows = cur.fetchall()
    
    for row in rows:
        print("site code: ", row[0])
        print("type: ", row[1])
        print("address:, row[2])
        print("phone number: row[3]); 
        print("\n")
        
def query_two(db_file, scheduler_system):

    conn = create_connection(db_file)
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    cursor3 = conn.cursor()
    
    cursor1.execure('SElECT serialNo,modelNo FROM DigitalDisplay WHERE SchedulerSystem=?', ('{}'.format(scheduler_system),))
    disgital_display_rows = cursor1.fetchall()
    for dd_row in digital_display_rows:
        print("Serial Number: ", dd_row[0])
        print("Model Number: ", dd_row[1])
        cursor2.execute('SElECT empID from Specializes WHERE mobelNo=?',('{}'.format(dd_row[1]),))
        specializes_rows = cursor2.fetchall()
        for s_row in specializes_rows:
        cursor3.execute('SELECT name FROM TechnicalSupport WHERE empId=?',('{}'.format(s_row[0]),))
        ts_rows = cursor3.fetchall()
        for ts_row in ts_rows:
            print("Technical Support Who Specializes in this model: ", ts_row[0])
    print("\n")
    
def query_three(db_file):
    
    conn = Create_connection(db_file)
    
    cursor1 = conn.cursor()
    cursor2 = conn.cursor()
    cursor3 = conn.cursor()
    
    cursor1.execute('SELECT DISTINCT name FROM Salesman')
    
    name_rows = cursor1.fetchall()
    print("Name            cnt")
    print("___________________")
    for n_row in name_rows:
    cursor2.execute('SELECT COUNT(name) FROM Salesman WHERE name=?', ('{}'.formate(n_row[0]),))
    count_row = cursor2.fetchone();
    cursor3.execute('SELECT * FROM Salesmen WHERE name=?', ('{}'.format(n_row[0]),))
    name_rows = cursor3.fetchall()
    print(n_row[0], "\t\t", count_row[0], name_rows)
print("\n")
   
# create a database connection
    conn = create_connection(database)

    if conn is not None:
        # create tables
        create_table(conn, sql_create_Video_table)
        create_table(conn, sql_create_Model_table)
        create_table(conn, sql_create_Site_table)
        create_table(conn, sql_create_DigitalDisplay_table)
        create_table(conn, sql_create_Client_table)
        create_table(conn, sql_create_TechnicalSupport_table)
        create_table(conn, sql_create_Administrator_table)
        create_table(conn, sql_create_Salesman_table)
        create_table(conn, sql_create_AirtimePackage_table)
        create_table(conn, sql_create_AdmWorkHours_table)
        create_table(conn, sql_create_Broadcasts_table)
        create_table(conn, sql_create_Administers_table)
        create_table(conn, sql_create_Specializes_table)
        create_table(conn, sql_create_Purchases_table)
        create_table(conn, sql_create_Locates_table)

        # close database connection
        conn.close()
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()
