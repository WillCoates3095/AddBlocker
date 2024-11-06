from Functions import *

if __name__ == "__main__":
    root = tk.Tk()

    # Main Window
    root.geometry("500x500") # Width x Height
    root.title("Adblocker:") # Title of the window
    #root.iconbitmap("icon.ico") # Icon of the window
    #root.configure(bg="black") # Background color
    label = tk.Label(root, text="Hello There!", font=("Arial", 18))
    label.pack(padx=10, pady=10)
    tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(padx=10, pady=10)
    entry = tk.Entry(root, font=("Arial", 18))
    entry.pack(padx=10, pady=10)
    button = tk.Button(root, text="Submit", font=("Arial", 12), command=lambda: try_password(entry.get(), root))
    button.pack(padx=10, pady=10)

    root.mainloop()
