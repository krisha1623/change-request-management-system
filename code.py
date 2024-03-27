import tkinter as tk
from tkinter import messagebox
import admin_choice
import choice_page
import view_reqeusts
import sqlite3
from database import connect_db, close_db

conn, cursor = connect_db()

def save_changes(conn, text):
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO table2 (code) VALUES (?)", (text,))
        conn.commit()
        messagebox.showinfo("Saved", "Text saved successfully!")

    except sqlite3.Error as e:
        conn.rollback()
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def go_back(window, previous_page):
    window.destroy()
    if previous_page == "admin":
        admin_choice.open_admin_choice_page()
        print("Opening admin choice page.")
    elif previous_page == "team_member":
        choice_page.open_choice_page()
        print("Opening team member login page.")

def view_all_requests():
    view_reqeusts.open_view_requests_page()

def open_code_page(previous_page):
    def load_data_from_db():
        conn, cursor = connect_db()

        # Load the latest code from table2
        cursor.execute("SELECT code FROM table2 ORDER BY rowid DESC LIMIT 1")
        code_data = cursor.fetchone()
        if code_data:
            code_text = code_data[0]
            mid_text.delete("1.0", "end")  # Clear the text widget before inserting new text
            mid_text.insert("1.0", code_text)

        # Load the latest request and its deadline from table1
        cursor.execute("SELECT request, deadline FROM table1 ORDER BY rowid DESC LIMIT 1")
        request_data = cursor.fetchone()
        if request_data:
            request_text, deadline_text = request_data
            top_frame_label.config(text=f"Latest Request: {request_text} (Deadline: {deadline_text})")

        conn.close()

    window = tk.Tk()
    window.geometry("750x600")  # Set window size to 800x500
    window.title("Code Page")

    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=6)  # Increase weight for top frame
    window.grid_rowconfigure(1, weight=4)  # Decrease weight for mid frame
    window.grid_rowconfigure(2, weight=2)  # Increase weight for bottom frame

    top_frame = tk.Frame(window, bg="yellow")
    top_frame.grid(row=0, column=0, sticky="ew", pady=(20, 0))  # Increase top frame height

    top_frame_label = tk.Label(top_frame, text="", bg="yellow", fg="black", font=("Arial", 14))  # Increase font size
    top_frame_label.pack()

    mid_frame = tk.Frame(window, bg="white")
    mid_frame.grid(row=1, column=0, sticky="ew", pady=(10, 0))  # Reduce pady for mid frame

    bottom_frame = tk.Frame(window, bg="blue")
    bottom_frame.grid(row=3, column=0, sticky="ew")

    mid_scrollbar_y = tk.Scrollbar(mid_frame, orient="vertical")
    mid_scrollbar_x = tk.Scrollbar(mid_frame, orient="horizontal")
    mid_text = tk.Text(mid_frame, wrap="none", yscrollcommand=mid_scrollbar_y.set, xscrollcommand=mid_scrollbar_x.set,
                       font=("Arial", 12))  # Increase font size

    mid_text.grid(row=0, column=0, sticky="nsew")
    mid_scrollbar_y.grid(row=0, column=1, sticky="ns")
    mid_scrollbar_x.grid(row=1, column=0, sticky="ew")

    mid_scrollbar_y.config(command=mid_text.yview)
    mid_scrollbar_x.config(command=mid_text.xview)

    bottom_frame_top = tk.Frame(bottom_frame, bg="blue")
    bottom_frame_top.pack(fill="both", expand=True)

    def on_save_button_click():
        text_to_save = mid_text.get("1.0", "end-1c")
        conn, _ = connect_db()
        cursor = conn.cursor()
        cursor.execute("UPDATE table2 SET code = ?", (text_to_save,))
        conn.commit()
        messagebox.showinfo("Saved", "Text saved successfully!")
        load_data_from_db()  # Reload data from the database after saving

    save_button = tk.Button(bottom_frame_top, text="Save", bg="lightgrey", fg="black", width=15,
                            command=on_save_button_click, font=("Arial", 12))  # Increase font size
    save_button.pack(side="left", padx=(10, 5), pady=5)

    view_all_requests_button = tk.Button(bottom_frame_top, text="View All Requests", bg="lightgrey", fg="black",
                                         command=view_all_requests, font=("Arial", 12))  # Increase font size
    view_all_requests_button.pack(side="left", padx=(10, 5), pady=5)  # Placed in the bottom frame between Save and Back

    back_button = tk.Button(bottom_frame_top, text="Back", bg="lightgrey", fg="black", width=15,
                            command=lambda: go_back(window, previous_page), font=("Arial", 12))  # Increase font size
    back_button.pack(side="right", padx=(5, 10), pady=0)

    load_data_from_db()  # Load data from the database when the window opens
    window.mainloop()

# open_code_page("admin")




