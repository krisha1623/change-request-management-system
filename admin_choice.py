import tkinter as tk
import code
import edit_change_request

def open_code_page(window):
    window.destroy()
    code.open_code_page("admin")

def open_add_change_request():
    # Functionality for adding change request
    print("Adding change request...")

def open_edit_change_request():
    # Functionality for editing change request
    print("Editing change request...")

def open_delete_change_request():
    # Functionality for deleting change request
    print("Deleting change request...")

def open_admin_login_page_and_close_current(window):
    import admin_page
    window.destroy()
    admin_page.open_admin_login_page()

def open_admin_choice_page():
    window = tk.Tk()
    window.title("Admin Choice Page")

    # Set window size and background color
    window.geometry("800x500")
    window.configure(bg="purple")

    # Create a frame to hold the buttons
    frame = tk.Frame(window, bg="purple")
    frame.pack(expand=True)

    # Configure font and button size
    button_font = ("Arial", 16)
    button_width = 20
    button_height = 2

    # Button for editing code
    edit_code_button = tk.Button(frame, text="Edit Code", command=lambda: open_code_page(window), font=button_font, width=button_width, height=button_height)
    edit_code_button.pack(pady=20)

    # Button for editing change request
    edit_change_request_button = tk.Button(frame, text="Edit Change Request", command=edit_change_request.open_edit_change_request_page, font=button_font, width=button_width, height=button_height)
    edit_change_request_button.pack(pady=20)

    # Back button
    back_button = tk.Button(frame, text="Back", command=lambda: open_admin_login_page_and_close_current(window), font=button_font, width=button_width, height=button_height)
    back_button.pack(pady=20)

    # Center the window on the screen
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

    window.mainloop()

# open_admin_choice_page()