import tkinter as tk
import admin_choice
import choice_page

def go_back(window):
    window.destroy()
    choice_page.open_choice_page()

def verify_login(username, password, project_title):
    if username == "admin" and password == "password" and project_title == "project1":
        return True
    else:
        return False

def login(username, password, project_title, window, error_label):
    if verify_login(username, password, project_title):
        window.destroy()
        admin_choice.open_admin_choice_page()
    else:
        error_label.config(text="Invalid username or password")

def open_admin_login_page():
    window = tk.Tk()
    window.title("Admin Login")
    window.geometry("800x500")

    # Set background color for the window
    window_color = "lightblue"
    window.configure(bg=window_color)

    # Create a frame to hold the components
    frame = tk.Frame(window, padx=20, pady=20, bg="lightblue")  # Set inner box color to off-white
    frame.pack(expand=True)

    username_label = tk.Label(frame, text="Admin Username:", font=("Arial", 16), bg="lightblue")  # Set label background color
    username_label.grid(row=0, column=0, pady=5, sticky="e")

    username_entry = tk.Entry(frame, font=("Arial", 16))
    username_entry.grid(row=0, column=1, pady=5, padx=10)

    password_label = tk.Label(frame, text="Admin Password:", font=("Arial", 16), bg="lightblue")  # Set label background color
    password_label.grid(row=1, column=0, pady=5, sticky="e")

    password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
    password_entry.grid(row=1, column=1, pady=5, padx=10)

    project_title_label = tk.Label(frame, text="Project Name:", font=("Arial", 16), bg="lightblue")  # Set label background color
    project_title_label.grid(row=2, column=0, pady=(5, 0), sticky="e")  # Adjusted pady for the Project Name label

    project_title_entry = tk.Entry(frame, font=("Arial", 16))
    project_title_entry.grid(row=2, column=1, pady=(5, 0), padx=10)  # Adjusted pady for the Project Name entry

    error_label = tk.Label(frame, text="", fg="red", font=("Arial", 12), bg="lightblue")  # Set label background color
    error_label.grid(row=3, columnspan=2, pady=10)

    login_button = tk.Button(frame, text="Login", command=lambda: login(username_entry.get(), password_entry.get(), project_title_entry.get(), window, error_label), font=("Arial", 12), width=6, height=1)  # Decreased button size
    login_button.grid(row=4, column=0, columnspan=2, pady=(5, 10))  # Adjusted pady for the Login button

    back_button = tk.Button(frame, text="Back", command=lambda: go_back(window), font=("Arial", 12), width=6, height=1)  # Decreased button size
    back_button.grid(row=5, column=0, columnspan=2, pady=10)

    window.mainloop()

# open_admin_login_page()