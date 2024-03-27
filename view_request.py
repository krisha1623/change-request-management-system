import tkinter as tk
from tkinter import messagebox
from database import connect_db, close_db

def open_view_requests_page():
    window = tk.Tk()
    window.title("View Requests Page")
    window.geometry("800x500")  # Set window size to 800x500
    window.configure(bg="lightblue")  # Set background color

    # Create a label for the page title
    title_label = tk.Label(window, text="View Requests", font=("Arial", 18))
    title_label.pack(pady=20)

    # Create a frame to hold the table
    table_frame = tk.Frame(window, bg="white")
    table_frame.pack()

    # Create a table header
    headers = ("SRNO/ID", "Request", "Deadline", "Time of Request")
    for col, header in enumerate(headers):
        header_label = tk.Label(table_frame, text=header, font=("Arial", 14, "bold"), padx=20, pady=10, borderwidth=1, relief="solid")
        header_label.grid(row=0, column=col, sticky="nsew")

    # Connect to the database and fetch data from Table1
    conn, cursor = connect_db()
    cursor.execute("SELECT id, request, deadline, time_of_request FROM table1")
    requests = cursor.fetchall()

    if not requests:
        # Display message if there are no requests
        no_requests_label = tk.Label(window, text="No requests found.", font=("Arial", 12))
        no_requests_label.pack(pady=20)
    else:
        # Display the fetched requests in the table
        for row, request in enumerate(requests, start=1):
            for col, value in enumerate(request):
                cell_label = tk.Label(table_frame, text=value, padx=20, pady=10, borderwidth=1, relief="solid")
                cell_label.grid(row=row, column=col, sticky="nsew")

    close_db(conn, cursor)

    # Create a button to close the page
    close_button = tk.Button(window, text="Close", command=window.destroy, font=("Arial", 14))
    close_button.pack(pady=30)

    window.mainloop()

# open_view_requests_page()