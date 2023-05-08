import sqlite3
from contextlib import closing
import tkinter as tk
from tkinter import messagebox, simpledialog


'''The connect_to_database function takes a database_name argument and tries to establish
 a connection with an SQLite database with the given name. If successful, it prints a
   success message and returns the connection object. If it fails, it prints an error message and returns None.'''


def connect_to_database(database_name):
    try:
        conn = sqlite3.connect(database_name)
        print("Connected to database successfully!")
        return conn
    except sqlite3.Error as e:
        print(f"Failed to connect to database: {e}")
        return None


'''The DigitalDisplayApp class inherits from tk.Tk and defines a GUI application with several buttons and a text widget.
 The __init__ method initializes the application window with a title, geometry, and initializes the conn attribute to
   None. The create_widgets method creates a frame for the buttons, creates the buttons, and a text widget to display
     the results of the user's actions.'''

class DigitalDisplayApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Display Manager- Intended For ABC.sqlite")
        self.geometry("800x400")

        self.conn = None

        self.create_widgets()
    '''The create_widgets method creates the GUI elements for the application.
 It creates a tk.Frame object and places it in the top left corner of the main window 
 (self) using the grid method. It then creates six buttons inside this frame, one for each action
   that can be performed by the user: display all digital displays, search for digital displays, insert a new digital display,
     delete a digital display, update a digital display, and quit the application. Each button is created using the 
     tk.Button method, with a text label and a command that specifies which method should be called when the button
       is clicked. The buttons are then placed in the options frame using the grid method, with each button given a row
         and column index. The sticky parameter specifies how the widget should align within its cell. The pady parameter
    adds padding between the buttons.'''
    def create_widgets(self):
        options_frame = tk.Frame(self)
        options_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

        tk.Button(options_frame, text="1. Display all the digital displays.", command=self.display_all_displays).grid(row=0, column=0, sticky='ew', pady=2)
        tk.Button(options_frame, text="2. Search digital displays given a scheduler system.", command=self.search_by_scheduler).grid(row=1, column=0, sticky='ew', pady=2)
        tk.Button(options_frame, text="3. Insert a new digital display.", command=self.insert_display).grid(row=2, column=0, sticky='ew', pady=2)
        tk.Button(options_frame, text="4. Delete a digital display.", command=self.delete_display).grid(row=3, column=0, sticky='ew', pady=2)
        tk.Button(options_frame, text="5. Update a digital display.", command=self.update_display).grid(row=4, column=0, sticky='ew', pady=2)
        tk.Button(options_frame, text="6. Quit.", command=self.quit_app).grid(row=5, column=0, sticky='ew', pady=2)

        # Create a Text widget to display the results
        self.result_text = tk.Text(self, wrap=tk.WORD)
        self.result_text.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def display_result(self, text):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)



    def display_all_displays(self):
        with closing(self.conn.cursor()) as c:
            c.execute("SELECT * FROM DigitalDisplay")
            rows = c.fetchall()

        result = '\n'.join(map(str, rows))
        self.display_result(result)

        choice = messagebox.askyesno("Model Details", "Do you want to see the model details of a display?")
        if choice:
            self.display_model_details()

    def display_model_details(self):
        serial_no = simpledialog.askstring("Serial Number", "Enter the serial number of the display:")

        with closing(self.conn.cursor()) as c:
            c.execute("""
                SELECT Model.* FROM Model, DigitalDisplay 
                WHERE DigitalDisplay.modelNo = Model.modelNo AND DigitalDisplay.serialNo = ?
            """, (serial_no,))
            rows = c.fetchall()

        result = '\n'.join(map(str, rows))
        self.display_result(result)

    def search_by_scheduler(self):
        scheduler_system = simpledialog.askstring("Scheduler System", "Enter the scheduler system to search for:")

        with closing(self.conn.cursor()) as c:
            c.execute("SELECT * FROM DigitalDisplay WHERE schedulerSystem = ?", (scheduler_system,))
            rows = c.fetchall()

        result = '\n'.join(map(str, rows))
        self.display_result(result)

    def insert_display(self):
        model_no = simpledialog.askstring("Model Number", "Enter the model number of the display:")
        scheduler_system = simpledialog.askstring("Scheduler System", "Enter the scheduler system of the display:")
        serial_no = simpledialog.askstring("Serial Number", "Enter the serial number of the display:")

        '''The code is inserting new data into the DigitalDisplay table in the database using an SQL query, committing the changes, 
and then calling the display_all_displays() method to update the display of all digital displays in the GUI. The with closing
 statement is used to automatically close the cursor after executing the SQL query, to ensure that resources are properly released.'''
        with closing(self.conn.cursor()) as c:
            c.execute("""
                INSERT INTO DigitalDisplay (serialNo, schedulerSystem, modelNo) VALUES (?, ?, ?)
            """, (serial_no, scheduler_system, model_no))
            self.conn.commit()

        self.display_all_displays()

    def delete_display(self):
        self.display_all_displays()

        serial_no = simpledialog.askstring("Serial Number", "Enter the serial number of the display to delete:")
        model_no = ""



    def delete_display(self):
        self.display_all_displays()

        serial_no = simpledialog.askstring("Serial Number", "Enter the serial number of the display to delete:")
        model_no = ""

        with closing(self.conn.cursor()) as c:
            c.execute("SELECT modelNo FROM DigitalDisplay WHERE serialNo = ?", (serial_no,))
            model_no = c.fetchone()[0]

            c.execute("DELETE FROM DigitalDisplay WHERE serialNo = ?", (serial_no,))
            self.conn.commit()

            c.execute("SELECT COUNT(*) FROM DigitalDisplay WHERE modelNo = ?", (model_no,))
            count = c.fetchone()[0]

            if count == 0:
                c.execute("DELETE FROM Model WHERE modelNo = ?", (model_no,))
                self.conn.commit()
                print("Model deleted successfully!")

        self.display_all_displays()

    def update_display(self):
        self.display_all_displays()

        serial_no = simpledialog.askstring("Serial Number", "Enter the serial number of the display to update:")
        new_scheduler_system = simpledialog.askstring("New Scheduler System", "Enter the new scheduler system of the display:")

        with closing(self.conn.cursor()) as c:
            c.execute("UPDATE DigitalDisplay SET schedulerSystem = ? WHERE serialNo = ?", (new_scheduler_system, serial_no))
            self.conn.commit()

        self.display_all_displays()

    def connect_to_database_gui(self):
        database_name = simpledialog.askstring("Database Name", "Enter database name:")
        self.conn = connect_to_database(database_name)

    def quit_app(self):
        if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
            if self.conn:
                self.conn.close()
            self.destroy()

    def run(self):      
        self.connect_to_database_gui()
        if self.conn is None:
            messagebox.showerror("Error", "Failed to connect to the database.")
            return
        self.mainloop()
''' #####################MAIN RUN#######################################'''
if __name__ == '__main__':
    app = DigitalDisplayApp()
    app.run()









