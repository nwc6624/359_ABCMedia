import sqlite3
from contextlib import closing
from enum import Enum, auto

class MenuOption(Enum):
    DISPLAY_ALL = auto()
    SEARCH_BY_SCHEDULER = auto()
    INSERT_DISPLAY = auto()
    DELETE_DISPLAY = auto()
    UPDATE_DISPLAY = auto()
    QUIT = auto()

def connect_to_database(database_name):
    """Connect to a SQLite database with the given name."""
    try:
        conn = sqlite3.connect(database_name)
        print("Connected to database successfully!")
        return conn
    except sqlite3.Error as e:
        print(f"Failed to connect to database: {e}")
        return None

def get_user_choice():
    """Get the user's choice from the menu options."""
    print("1. Display all the digital displays.")
    print("2. Search digital displays given a scheduler system.")
    print("3. Insert a new digital display.")
    print("4. Delete a digital display.")
    print("5. Update a digital display.")
    print("6. Quit.")

    choice = int(input("Enter your choice (1-6): "))
    return MenuOption(choice)

def display_all_displays(conn):
    """Display all records in the DigitalDisplay table."""
    with closing(conn.cursor()) as c:
        c.execute("SELECT * FROM DigitalDisplay")
        rows = c.fetchall()

    for row in rows:
        print(row)

    choice = input("Do you want to see the model details of a display? (y/n): ")
    if choice.lower() == "y":
        display_model_details(conn)

def display_model_details(conn):
    """Display model details of a display with a given serial number."""
    serial_no = input("Enter the serial number of the display: ")

    with closing(conn.cursor()) as c:
        c.execute("""
            SELECT Model.* FROM Model, DigitalDisplay 
            WHERE DigitalDisplay.modelNo = Model.modelNo AND DigitalDisplay.serialNo = ?
        """, (serial_no,))
        rows = c.fetchall()

    for row in rows:
        print(row)

def search_by_scheduler(conn):
    """Search for digital displays with a given scheduler system."""
    scheduler_system = input("Enter the scheduler system to search for: ")

    with closing(conn.cursor()) as c:
        c.execute("SELECT * FROM DigitalDisplay WHERE schedulerSystem = ?", (scheduler_system,))
        rows = c.fetchall()

    for row in rows:
        print(row)

def insert_display(conn):
    """Insert a new digital display with the given data."""
    model_no = input("Enter the model number of the display: ")
    scheduler_system = input("Enter the scheduler system of the display: ")
    serial_no = input("Enter the serial number of the display: ")

    with closing(conn.cursor()) as c:
        c.execute("""
            INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo) VALUES (?, ?, ?)
        """, (serial_no, scheduler_system, model_no))
        conn.commit()

    display_all_displays(conn)

def delete_display(conn):
    """Delete a digital display with a given serial number."""
    display_all_displays(conn)

    serial_no = input("Enter the serial number of the display to delete: ")
    model_no = ""

    with closing(conn.cursor()) as c:
                c.execute("SELECT modelNo FROM DigitalDisplay WHERE serialNo = ?", (serial_no,))
    model_no = c.fetchone()[0]

    c.execute("DELETE FROM DigitalDisplay WHERE serialNo = ?", (serial_no,))
    conn.commit()

    c.execute("SELECT COUNT(*) FROM DigitalDisplay WHERE modelNo = ?", (model_no,))
    count = c.fetchone()[0]

    if count == 0:
            c.execute("DELETE FROM Model WHERE modelNo = ?", (model_no,))
            conn.commit()
            print("Model deleted successfully!")

    display_all_displays(conn)

def update_display(conn):
    """Update the scheduler system of a digital display with a given serial number."""
    display_all_displays(conn)

    serial_no = input("Enter the serial number of the display to update: ")
    new_scheduler_system = input("Enter the new scheduler system of the display: ")

    with closing(conn.cursor()) as c:
        c.execute("UPDATE DigitalDisplay SET schedulerSystem = ? WHERE serialNo = ?", (new_scheduler_system, serial_no))
        conn.commit()

    display_all_displays(conn)

def main():
    conn = None

    while True:
        if conn is None:
            database_name = input("Enter database name: ")
            conn = connect_to_database(database_name)

        choice = get_user_choice()

        if choice == MenuOption.DISPLAY_ALL:
            display_all_displays(conn)
        elif choice == MenuOption.SEARCH_BY_SCHEDULER:
            search_by_scheduler(conn)
        elif choice == MenuOption.INSERT_DISPLAY:
            insert_display(conn)
        elif choice == MenuOption.DELETE_DISPLAY:
            delete_display(conn)
        elif choice == MenuOption.UPDATE_DISPLAY:
            update_display(conn)
        elif choice == MenuOption.QUIT:
            print("Exiting program.")
            conn.close()
            break
        else:
            print("Invalid choice. Please choose a number from 1-6.")

if __name__ == '__main__':
    main()
