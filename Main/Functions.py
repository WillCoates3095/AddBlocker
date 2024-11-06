import tkinter as tk

def try_password(password, root):
    if password == "password":
        print("Correct Password")
        clear_screen(root)
        home_screen(root)
    else:
        print("Incorrect Password")

def home_screen(root):
    main_label = tk.Label(root, text="Welcome!", font=("Arial", 18))
    main_label.pack(padx=10, pady=10)
    button = tk.Button(root, text="Start Addblock!", font=("Arial", 18))
    button.pack(padx=10, pady=10)

def clear_screen(root):
    for widget in root.winfo_children():
        widget.destroy()
def print_input(entry):
    print(entry.get())