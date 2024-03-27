import tkinter as tk
from tkinter import messagebox

from database import connect_db, close_db
import sqlite3
import datetime

#back
def open_admin_choice(window):
    import admin_choice
    window.destroy()
    admin_choice.open_admin_choice_page()

def is_valid_datetime(datetime_str):
    try:
        datetime.datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S')  # Assuming the datetime format is YYYY-MM-DD HH:MM:SS
        return True
    except ValueError:
        return False

# Save change request function
def save_change_request():
    # Get change request text and deadline datetime from entry fields
    change_request_text = change_request_entry.get("1.0", "end-1c")
    deadline_datetime = deadline_entry.get()

    # Check if the deadline datetime is in the appropriate format
    if not is_valid_datetime(deadline_datetime):
        messagebox.showerror("Error", "Please enter the deadline in the format YYYY-MM-DD HH:MM:SS.")
        return  # Stop execution if the datetime format is incorrect

    # Connect to the database
    conn, cursor = connect_db()

    try:
        # Insert the change request into the database
        cursor.execute("INSERT INTO table1 (request, deadline) VALUES (?, ?)",
                       (change_request_text, deadline_datetime))
        conn.commit()

        # Close the connection
        close_db(conn, cursor)

        # Show success message
        messagebox.showinfo("Saved", "Change request saved successfully!")

    except sqlite3.Error as e:
        # Rollback changes if an error occurs
        conn.rollback()

        # Show error message
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

    finally:
        close_db(conn, cursor)

def update_change_request():
    # Create a new window for updating the change request
    update_window = tk.Toplevel()
    update_window.title("Update Change Request")

    # Configure window size and background color
    update_window.geometry("800x500")
    update_window.configure(bg="pink")

    # Function to center the window on the screen
    def center_window():
        update_window.update_idletasks()
        width = update_window.winfo_width()
        height = update_window.winfo_height()
        x = (update_window.winfo_screenwidth() // 2) - (width // 2)
        y = (update_window.winfo_screenheight() // 2) - (height // 2)
        update_window.geometry(f"{width}x{height}+{x}+{y}")

    # Label and Entry for ID/Sr. No
    id_label = tk.Label(update_window, text="Enter ID/Sr. No:", font=("Arial", 12),bg="pink")  # Increase font size
    id_label.pack(pady=(40, 5))
    id_entry = tk.Entry(update_window)
    id_entry.pack(pady=(0, 10))

    # Function to fetch the existing request and deadline
    def fetch_request():
        # Get the ID/Sr. No from the entry field
        request_id = id_entry.get()

        # Connect to the database
        conn, cursor = connect_db()

        try:
            # Fetch the existing request and deadline from the database using the ID/Sr. No
            cursor.execute("SELECT request, deadline FROM table1 WHERE id = ?", (request_id,))
            row = cursor.fetchone()

            if row:
                existing_request, existing_deadline = row

                # Display the existing request and deadline for confirmation
                existing_request_label = tk.Label(update_window, text=f"Existing Request: {existing_request}",
                                                  bg="pink")  # Set label background as window background
                existing_request_label.pack()
                existing_deadline_label = tk.Label(update_window, text=f"Existing Deadline: {existing_deadline}",
                                                   bg="pink")  # Set label background as window background
                existing_deadline_label.pack()

                # Entry fields for updating the request and deadline
                new_request_label = tk.Label(update_window, text="New Request:", font=("Arial", 12),bg="pink")  # Increase font size
                new_request_label.pack(pady=(25, 5))
                new_request_entry = tk.Text(update_window, height=5, width=60)
                new_request_entry.insert(tk.END, existing_request)  # Pre-fill with existing request
                new_request_entry.pack()

                new_deadline_label = tk.Label(update_window, text="New Deadline (YYYY-MM-DD HH:MM:SS):",
                                               font=("Arial", 12),bg="pink")  # Increase font size
                new_deadline_label.pack(pady=(20, 5))
                new_deadline_entry = tk.Entry(update_window)
                new_deadline_entry.insert(tk.END, existing_deadline)  # Pre-fill with existing deadline
                new_deadline_entry.pack()

                # Function to update the request and deadline in the database
                def update_in_db():
                    # Get the new request and deadline from the entry fields
                    new_request_text = new_request_entry.get("1.0", "end-1c")
                    new_deadline_datetime = new_deadline_entry.get()

                    # Check if the new deadline datetime is in the appropriate format
                    if not is_valid_datetime(new_deadline_datetime):
                        messagebox.showerror("Error", "Please enter the deadline in the format YYYY-MM-DD HH:MM:SS.")
                        return  # Stop execution if the datetime format is incorrect

                    # Connect to the database
                    conn, cursor = connect_db()

                    try:
                        # Update the request and deadline in the database
                        cursor.execute("UPDATE table1 SET request = ?, deadline = ? WHERE id = ?",
                                       (new_request_text, new_deadline_datetime, request_id))
                        conn.commit()

                        # Close the connection
                        close_db(conn, cursor)

                        # Show success message
                        messagebox.showinfo("Updated", "Change request and deadline updated successfully!")

                        # Close the update window
                        update_window.destroy()


                    except sqlite3.Error as e:
                        conn, cursor = connect_db()
                        # Rollback changes if an error occurs
                        conn.rollback()

                        # Show error message
                        messagebox.showerror("Error", f"An error occurred: {str(e)}")

                        # Close the connection
                        close_db(conn, cursor)

                # Button to update the request and deadline
                update_button = tk.Button(update_window, text="Update", command=update_in_db,
                                          font=("Arial", 12))  # Increase font size
                update_button.pack(pady=(30, 20))

            else:
                # ID/Sr. No not found in the database
                messagebox.showerror("Error", "ID/Sr. No not found!")

        except sqlite3.Error as e:
            # Rollback changes if an error occurs
            conn.rollback()

            # Show error message
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        finally:
            close_db(conn, cursor)

    # Button to fetch the existing request and deadline
    fetch_button = tk.Button(update_window, text="Fetch", command=fetch_request, font=("Arial", 12))  # Increase font size
    fetch_button.pack(pady=(30, 20))

    # Center the window on the screen
    center_window()

    update_window.mainloop()



def delete_change_request():
    # Create a new window for deleting a change request
    delete_window = tk.Toplevel()
    delete_window.title("Delete Change Request")

    # Configure window size and background color
    delete_window.geometry("800x500")
    delete_window.configure(bg="lightblue")

    # Label and Entry for ID/Sr. No
    id_label = tk.Label(delete_window, text="Enter ID/Sr. No:", font=("Arial", 18), bg="lightblue")
    id_label.pack(pady=(100, 5))
    id_entry = tk.Entry(delete_window, font=("Arial", 18))
    id_entry.pack(pady=(30, 10))

    # Function to delete the change request from the database
    def delete_from_db():
        # Get the ID/Sr. No from the entry field
        request_id = id_entry.get()

        # Connect to the database
        conn, cursor = connect_db()

        try:
            # Check if the ID/Sr. No exists in the database
            cursor.execute("SELECT id FROM table1 WHERE id = ?", (request_id,))
            row = cursor.fetchone()

            if row:
                # ID/Sr. No found, proceed with deletion
                cursor.execute("DELETE FROM table1 WHERE id = ?", (request_id,))
                conn.commit()

                # Show success message
                messagebox.showinfo("Deleted", "Change request deleted successfully!")

                # Close the delete window
                delete_window.destroy()

            else:
                # ID/Sr. No not found in the database
                messagebox.showerror("Error", "ID/Sr. No not found!")



        except sqlite3.Error as e:
            # Rollback changes if an error occurs
            conn.rollback()

            # Show error message
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

        finally:
            # Close the delete window
            delete_window.destroy()
            # Close the connection
            close_db(conn, cursor)

    # Button to delete the change request
    delete_button = tk.Button(delete_window, text="Delete", command=delete_from_db, font=("Arial", 12))
    delete_button.pack(pady=(10, 20))

    delete_window.mainloop()

def open_edit_change_request_page():
    window = tk.Tk()
    window.title("Change Request Page")

    # Configure window size and background color
    window.geometry("800x500")
    window.configure(bg="brown")

    # Function to center the window on the screen
    def center_window():
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f"{width}x{height}+{x}+{y}")

    change_request_label = tk.Label(window, text="Change Request:", font=("Arial", 18), bg=window["bg"])
    change_request_label.pack(pady=(20, 10))
    global change_request_entry  # Declare as global variable
    change_request_entry = tk.Text(window, height=10, width=60)
    change_request_entry.pack(pady=(0, 20))

    deadline_label = tk.Label(window, text="Deadline (Date, format: YYYY-MM-DD HH:MM:SS):", font=("Arial", 18), bg=window["bg"])  # Specify the format here
    deadline_label.pack(pady=(20, 10))
    global deadline_entry  # Declare as global variable
    deadline_entry = tk.Entry(window, font=("Arial", 20))

    deadline_entry.pack(pady=(0, 20))

    save_button = tk.Button(window, text="Save", command=save_change_request, font=("Arial", 14), width=10, height=1)
    save_button.pack(side="left", padx=(20, 20))

    update_button = tk.Button(window, text="Update", command=update_change_request, font=("Arial", 14), width=10, height=1)
    update_button.pack(side="left", padx=(10, 20))

    delete_button = tk.Button(window, text="Delete", command=delete_change_request, font=("Arial", 14), width=10, height=1)
    delete_button.pack(side="left", padx=(10, 20))

    back_button = tk.Button(window, text="Back", command=lambda: open_admin_choice(window), font=("Arial", 14), width=10, height=1)
    back_button.pack(side="left", padx=(100, 20))

    # Center the window on the screen
    center_window()

    window.mainloop()

# open_edit_change_request_page()