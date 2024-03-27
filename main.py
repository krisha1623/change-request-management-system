import tkinter as tk
import choice_page
def open_choice_page_and_close_current():

    window.destroy()
    choice_page.open_choice_page()

window = tk.Tk()
window.title("Main Page")

# Configure window size
window.geometry("800x500")  # Set window size to 800x500 pixels

# Create a canvas covering the entire window
canvas = tk.Canvas(window, width=800, height=500)
canvas.pack()

# Draw rectangles with different colors to create a dual-color background
canvas.create_rectangle(0, 0, 400, 500, fill="red")  # Left half of the window
canvas.create_rectangle(400, 0, 800, 500, fill="black")  # Right half of the window

# Add a label for Change Request Management System
label_text = "Change Request Management System"
label = tk.Label(window, text=label_text, font=("Arial", 30), fg="black", bg="white")  # Black text, white background
label.place(relx=0.5, rely=0.1, anchor="center")  # Place in the middle horizontally and 10% from the top vertically

login_button = tk.Button(window, text="Click here to login", command=open_choice_page_and_close_current,
                          font=("Arial", 16))  # Increase font size

# Calculate the center position for the button
button_width = 200  # Adjust button width as needed
button_height = 50  # Adjust button height as needed
button_x_position = (800 // 2) - (button_width // 2)
button_y_position = (500 // 2) - (button_height // 2)

# Place the button at the center of the window
login_button.place(x=button_x_position, y=button_y_position, width=button_width, height=button_height)

window.mainloop()