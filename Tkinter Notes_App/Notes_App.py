import tkinter as tk  
from tkinter import messagebox
def save_note():
    note = text_area.get("1.0", tk.END)
    file = open("note.txt", "w")  
    file.write(note)
    file.close() 
    messagebox.showinfo("Saved", "Note Saved!")
def load_note():
    try:
        file = open("note.txt", "r") 
        note = file.read() 
        file.close() 
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, note) 
    except FileNotFoundError: 
        messagebox.showwarning("Not Found", "No note found!")  
# Main window
window = tk.Tk()
window.title("Notes Application")
window.geometry("800x600")
# Text area
text_area = tk.Text(window,font=("Times New Roman",14))
text_area.pack(expand=True ,fill='both')
# Button frame
button_frame = tk.Frame(window)
button_frame.pack(side='bottom', pady=20)
# Save button
save_btn = tk.Button(button_frame, text="Save Note", command=save_note)
save_btn.pack(side='left', padx=30)
# Load button
load_btn = tk.Button(button_frame, text="Load Note", command=load_note)
load_btn.pack(side='left', padx=30)
window.mainloop()
