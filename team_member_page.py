import tkinter as tk
import choice_page
import code

# Dummy function to verify team member login
def verify_login(username, password, project_title):
    # Replace this logic with your actual verification process
    if (username == "team_member1" and password == "password1" and project_title == "project1") or \
       (username == "team_member2" and password == "password2" and project_title == "project1") or \
       (username == "team_member3" and password == "password3" and project_title == "project1") or \
       (username == "team_member4" and password == "password4" and project_title == "project1"):
        return True
    else:
        return False

def go_back(window):
    window.destroy()
    choice_page.open_choice_page()

def open_code_page(window):
    window.destroy()
    code.open_code_page("team_member")

def open_team_member_login_page():
    window = tk.Tk()
    window.title("Team Member Login")

    # Configure window size
    window.geometry("800x500")  # Set window size to 800x500 pixels

    # Set light green background color for the entire screen
    window.configure(bg="light green")

    # Create a frame to hold the components with light green background
    frame = tk.Frame(window, padx=20, pady=20, bg="light green")  # Set frame background color
    frame.pack(expand=True)

    # Configure font and button size
    label_font = ("Arial", 16)
    entry_font = ("Arial", 14)
    button_font = ("Arial", 14)
    button_width = 10
    button_height = 1

    username_label = tk.Label(frame, text="Team Member Username:", font=label_font, bg="light green")  # Set label background color
    username_label.grid(row=0, column=0, padx=10, pady=5)

    username_entry = tk.Entry(frame, font=entry_font)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    password_label = tk.Label(frame, text="Team Member Password:", font=label_font, bg="light green")  # Set label background color
    password_label.grid(row=1, column=0, padx=10, pady=5)

    password_entry = tk.Entry(frame, show="*", font=entry_font)
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    project_title_label = tk.Label(frame, text="Project Name:", font=label_font, bg="light green")  # Set label background color
    project_title_label.grid(row=2, column=0, padx=10, pady=5)

    project_title_entry = tk.Entry(frame, font=entry_font)
    project_title_entry.grid(row=2, column=1, padx=10, pady=5)

    error_label = tk.Label(frame, text="", fg="red", bg="light green")  # Set label background color
    error_label.grid(row=3, columnspan=2, padx=10, pady=5)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        project_title = project_title_entry.get()
        if verify_login(username, password, project_title):
            open_code_page(window)
        else:
            error_label.config(text="Invalid username or password")

    login_button = tk.Button(frame, text="Login", command=login, font=button_font, width=button_width, height=button_height)
    login_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    back_button = tk.Button(frame, text="Back", command=lambda: go_back(window), font=button_font, width=button_width, height=button_height)
    back_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    window.mainloop()

# Call the function to open the login page
# open_team_member_login_page()