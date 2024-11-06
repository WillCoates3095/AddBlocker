import tkinter as tk

root = tk.Tk()

# Main Window
root.geometry("500x500") # Width x Height
root.title("Adblocker:") # Title of the window
#root.iconbitmap("icon.ico") # Icon of the window
#root.configure(bg="black") # Background color
label = tk.Label(root, text="Hello World", font=("Arial", 18))
label.pack(padx=10, pady=10)
entry = tk.Entry(root, font=("Arial", 18))
entry.pack(padx=10, pady=10)

root.mainloop()
