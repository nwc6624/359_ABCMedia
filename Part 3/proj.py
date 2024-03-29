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

def question1(conn):
    # Count the number of distinct site codes in the Locates table
    c = conn.cursor()
    c.execute("SELECT COUNT(DISTINCT siteCode) FROM Locates")
    result = c.fetchone()[0]
    print(f"There are {result} distinct site codes in the Locates table.")


def question2(conn, model_no):
    # Retrieve the weight of the given model number from the Model table
    c = conn.cursor()
    c.execute(f"SELECT weight FROM Model WHERE modelNo = '{model_no}'")
    result = c.fetchone()[0]
    print(f"The weight of Model {model_no} is {result}.")

def question3(conn, site_code):
    # Retrieve the number of digital displays located at the given site code
    c = conn.cursor()
    c.execute(f"SELECT COUNT(serialNo) FROM Locates WHERE siteCode = {site_code}")
    result = c.fetchone()[0]
    print(f"There are {result} digital displays located at Site {site_code}.")


def main(question_num):
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

     
        if question_num == "1":
            question1(conn)
        elif question_num == "2":
            model_no = input("Enter model number: ")
            question2(conn, model_no)
        elif question_num == "3":
            site_code = input("Enter site code: ")
            question3(conn, site_code)
        else:
            print("Invalid question number.")
    else:
        print("Error! cannot create the database connection.")

        # close database connection
        conn.close()

if __name__ == '__main__':
    question_num = input("Enter question number (1-3): ")
    main(question_num)
