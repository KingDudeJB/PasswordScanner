#https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/
#https://flatuicolors.com/
import tkinter as tk
from tkinter import messagebox
from PasswordSC import PWC  # Import the password checking function

def create_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Password Strength Checker")
    root.geometry("500x350")
    
    root.config(bg="#2c3e50")
     
    # Label for password entry
    label = tk.Label(root, text="Enter a password/ text:", bg="#2c3e50", fg="#ecf0f1")
    label.pack(pady=10)
    
    # Password entry field
    password_entry = tk.Entry(root, show="*", width=30)
    password_entry.pack(pady=5)

    # Function to check the entered password and display result
    def check_password():
        entered_password = password_entry.get()
        result = PWC(entered_password)
        messagebox.showinfo("Password Strength", result)
        
    # Button to check password strength
    submit_button = tk.Button(root, text="Check Strength", command=check_password,
                              bg="#f1c40f", fg="#2c3e50",  # Initial background and text color
                              relief="raised",  # Raised effect
                              bd=5,  # Border width
                              font=("Arial", 12, "bold"),
                              activebackground="#45a049",  # Color when active (button is pressed)
                              activeforeground="white")  # Text color when button is pressed
    submit_button.pack(pady=20)

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    create_gui()

