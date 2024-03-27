import tkinter as tk

def open_admin_login_page_and_close_current(window):
    import admin_page
    window.destroy()
    admin_page.open_admin_login_page()

def open_team_member_login_page_and_close_current(window):
    import team_member_page
    window.destroy()
    team_member_page.open_team_member_login_page()

def open_choice_page():
    window = tk.Tk()
    window.title("Login Choice")

    # Set window size and background color
    window.geometry("800x500")
    window.configure(bg="blue")

    # Configure frame background color
    frame = tk.Frame(window, width=800, height=500, bg="blue")
    frame.pack(expand=True)

    # Configure font and button size
    button_font = ("Arial", 16)
    button_width = 20
    button_height = 2

    admin_button = tk.Button(frame, text="Admin", command=lambda: open_admin_login_page_and_close_current(window), font=button_font, width=button_width, height=button_height)
    admin_button.pack(pady=20)

    team_member_button = tk.Button(frame, text="Team Member", command=lambda: open_team_member_login_page_and_close_current(window), font=button_font, width=button_width, height=button_height)
    team_member_button.pack(pady=20)

    window.mainloop()

# open_choice_page()