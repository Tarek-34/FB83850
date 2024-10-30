# Customer Feedback Application

This is a simple Python application that allows users to submit feedback through a graphical user interface (GUI) built with `tkinter`. The feedback is stored in an SQLite database, and authorized users can print the stored feedback via the console.

---

## Features

- **Submit Feedback:** Users can enter their name, email, and feedback through the GUI.
- **Data Storage:** Feedback is saved in an SQLite database (`customer_feedback.db`).
- **View Feedback:** Authorized users (with password) can print all feedback entries to the console.
- **GUI:** Built using the `tkinter` library for easy interaction.

---

## Requirements

- Python 3.x
- `tkinter` (comes pre-installed with Python)
- `sqlite3` (comes pre-installed with Python)

---

## Setup and Usage

### 1. Install Python  
Make sure you have Python 3 installed. You can download it from [Python's official website](https://www.python.org/).

### 2. Run the Program  
Clone the repository or copy the script to your local machine. Run the script with the following command:

```bash
python feedback_app.py
