
"""   Date: 5/10/2023
   Authors: Noah Caulfield
            Matt Mitchell
            
            Intended for use with ABC.sqlite, or equivalent build version
            
            Designed for CS 359 Part 4 Final Project
                        CMD_with_tkinter_gui.py                           """
            

import sqlite3
from contextlib import closing
import tkinter as tk
from tkinter import messagebox, simpledialog


def connect_to_database(database_name):
    try:
        conn = sqlite3.connect(database_name)
        print("Connected to database successfully!")
        return conn
    except sqlite3.Error as e:
        print(f"Failed to connect to database: {e}")
        return None


class DigitalDisplayApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Digital Display Manager")
        self.geometry("800x400")

        self.conn = None

        self.create_widgets()

    def create_widgets(self):
        options_frame = tk.Frame(self)
        options_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

        tk.Button(options_frame, text="1. Display all the digital displays.", command=self.display_all_displays).grid(row=0, column=0, sticky='ew', pady=2)
        tk.Button(options_frame, text="2. Search digital displays given a scheduler system.", command=self.search_by_scheduler).grid(row=1, column=0, sticky='ew', pady=2)
        tk.Button(options_frame, text="3. Insert a new digital display.", command=self.insert_display).grid(row=2, column=0, sticky='ew', pady=2)
        tk.Button(options_frame, text="4. Delete a digital display.", command=self.delete_display).grid(row=3, column=0, sticky='ew', pady=2)
        tk.Button(options_frame, text="5. Update a digital display.", command=self.update_display).grid(row=4, column=0, sticky='ew', pady=2)
        tk.Button(options_frame, text="6. Quit.", command=self.quit_app).grid(row=5, column=0, sticky='ew', pady=2)

        self.result_text = tk.Text(self, wrap=tk.WORD)
        self.result_text.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

    def display_result(self, headers, rows):
        result = "{:<15}".format(headers[0])
        result += "{:<20}".format(headers[1])
        if len(headers) > 2:
            result += "{:<15}".format(headers[2]) + "\n"
        else:
            result += "\n"
        result += "-" * 50 + "\n"

        for row in rows:
            result += "{:<15}".format(row[0] or "")
            result += "{:<20}".format(row[1] or "")
            if len(row) > 2:
                result += "{:<15}".format(row[2] or "") + "\n"
            else:
                result += "\n"

        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, result)




    def display_all_displays(self):
        with closing(self.conn.cursor()) as c:
            c.execute("SELECT * FROM DigitalDisplay")
            rows = c.fetchall()

        headers = ["Serial #", "Scheduler System", "Model #"]
        self.display_result(headers, rows)

        choice = messagebox.askyesno("Model Details", "Do you want to see the model details of a display?")
        if choice:
            self.display_model_details()

    def display_model_details(self):
        serial_no = simpledialog.askstring("Serial Number", "Enter the serial number of the display:")

        with closing(self.conn.cursor()) as c:
            c.execute("""
                SELECT Model.modelNo, Model.screenSize
                FROM Model
                INNER JOIN DigitalDisplay ON Model.modelNo = DigitalDisplay.modelNo
                WHERE DigitalDisplay.serialNo = ?
            """, (serial_no,))
            row = c.fetchone()

        if row:
            headers = ["Model No", "Screen Size"]
            rows = [row]
            self.display_result(headers, rows)
        else:
            messagebox.showinfo("No Results", "No model details found for the given serial number.")



    def search_by_scheduler(self):
        scheduler_system = simpledialog.askstring("Scheduler System", "Enter the scheduler system to search for:")

        with closing(self.conn.cursor()) as c:
            c.execute("SELECT * FROM DigitalDisplay WHERE schedulerSystem = ?", (scheduler_system,))
            rows = c.fetchall()

        headers = ["Serial #", "Scheduler System", "Model #"]
        self.display_result(headers, rows)


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









