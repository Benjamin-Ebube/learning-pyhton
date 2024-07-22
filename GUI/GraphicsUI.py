import tkinter as tk

root = tk.Tk()

root.geometry("800x500")
root.title("My first GUI")

# label is just text
label = tk.Label(root, text="Hello World", font=("Arial", 18))
# .pack is used for positioning using x,y parameters like in graph.
label.pack(padx=20, pady=50)

textbox


root.mainloop()