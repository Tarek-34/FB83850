import sqlite3
import tkinter as tk
from tkinter import messagebox
import getpass

# Initialize SQLite Database
def initialize_database():
    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            feedback TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Function to submit feedback to the database
def submit_feedback():
    name = name_entry.get()
    email = email_entry.get()
    feedback = feedback_entry.get("1.0", tk.END)

    if not name or not email or not feedback.strip():
        messagebox.showwarning("Warning", "All fields are required!")
        return

    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)
    ''', (name, email, feedback))
    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Feedback submitted!")
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    feedback_entry.delete("1.0", tk.END)

# Function to print all data (password protected)
def print_data():
    password = getpass.getpass("Enter the password to view data: ")

    if password != "pass":  # Replace with your desired password
        print("Incorrect password!")
        return

    conn = sqlite3.connect('customer_feedback.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("No feedback available.")
    else:
        for row in data:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Feedback: {row[3]}")

# Set up the GUI
root = tk.Tk()
root.title("Customer Feedback")

# Labels and input fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Email").grid(row=1, column=0, padx=10, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Feedback").grid(row=2, column=0, padx=10, pady=5)
feedback_entry = tk.Text(root, width=30, height=5)
feedback_entry.grid(row=2, column=1, padx=10, pady=5)

# Submit button
submit_button = tk.Button(root, text="Submit", command=submit_feedback)
submit_button.grid(row=3, column=0, columnspan=2, pady=10)

# Print data button (console)
print_button = tk.Button(root, text="Print Data", command=print_data)
print_button.grid(row=4, column=0, columnspan=2, pady=10)

# Initialize the database and run the GUI
initialize_database()
root.mainloop()
