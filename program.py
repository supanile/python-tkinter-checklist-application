from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# root window
root = Tk()
root.title("CheckList Application")

# Create PhotoImage for PNG file
try:
    icon = PhotoImage(file="icon/schedule.png")
    root.iconphoto(False, icon)
except:
    print("Icon file not found or failed to load")

root.geometry("500x600+500+100")
root.resizable(0,0)

# Colors and fonts used
BG_COLOR = "#f0f2f5"
ACCENT_COLOR = "#1a73e8"
BUTTON_BG = "#1a73e8"
BUTTON_FG = "white"
HOVER_COLOR = "#1557b0"

font_header = ("Helvetica", 20, "bold")
font_normal = ("Helvetica", 12)
font_button = ("Helvetica", 11)

root.config(bg=BG_COLOR)

def addItem():
    data = inputEntry.get()
    if data.strip():  # Check if there's non-empty text
        listbox.insert(END, data)
        inputEntry.delete(0, END)
    inputEntry.focus()  # Return focus to input field

def confirm_remove():
    selected = listbox.curselection()
    if selected:
        if messagebox.askyesno('Confirm Remove', 'Are you sure you want to remove this item?'):
            listbox.delete(selected)

def confirm_clear():
    if listbox.size() > 0:
        if messagebox.askyesno('Confirm Clear', 'Are you sure you want to clear all items?'):
            listbox.delete(0, END)

def confirm_quit():
    if messagebox.askyesno('Confirm Exit', 'Are you sure you want to exit?'):
        root.destroy()

# Create Style for ttk widgets
style = ttk.Style()
style.configure("Custom.TEntry", padding=10)
style.configure("Custom.TButton", 
    padding=10, 
    background=BUTTON_BG,
    foreground=BUTTON_FG,
    font=font_button
)

# Header Frame
header_frame = Frame(root, bg=ACCENT_COLOR, height=80)
header_frame.pack(fill=X)
header_frame.pack_propagate(False)

header_label = Label(
    header_frame, 
    text="To-do List", 
    font=font_header,
    bg=ACCENT_COLOR,
    fg="white"
)
header_label.pack(pady=20)

# Main Content Frame
main_frame = Frame(root, bg=BG_COLOR)
main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

# Input Frame
input_frame = Frame(main_frame, bg=BG_COLOR)
input_frame.pack(fill=X, pady=(0, 10))

inputEntry = ttk.Entry(
    input_frame,
    font=font_normal,
    style="Custom.TEntry",
)
inputEntry.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))

btnAdd = Button(
    input_frame,
    text="Add Item",
    font=font_button,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    relief="flat",
    command=addItem,
    cursor="hand2"
)
btnAdd.pack(side=RIGHT)

# Listbox Frame
listbox_frame = Frame(main_frame, bg=BG_COLOR)
listbox_frame.pack(fill=BOTH, expand=True)

# Create Scrollbar
scrollbar = Scrollbar(listbox_frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(
    listbox_frame,
    font=font_normal,
    bg="white",
    selectmode=SINGLE,
    activestyle="none",
    relief="flat",
    borderwidth=0,
    highlightthickness=1,
    highlightcolor=ACCENT_COLOR,
    yscrollcommand=scrollbar.set
)
listbox.pack(fill=BOTH, expand=True)

# Configure Scrollbar to work with Listbox
scrollbar.config(command=listbox.yview)

# Button Frame
button_frame = Frame(main_frame, bg=BG_COLOR)
button_frame.pack(fill=X, pady=(10, 0))

btnRemove = Button(
    button_frame,
    text="Remove Item",
    font=font_button,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    relief="flat",
    command=confirm_remove,  
    cursor="hand2"
)
btnRemove.pack(side=LEFT, padx=(0, 5))

btnClear = Button(
    button_frame,
    text="Clear All",
    font=font_button,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    relief="flat",
    command=confirm_clear,  
    cursor="hand2"
)
btnClear.pack(side=LEFT, padx=5)

btnQuit = Button(
    button_frame,
    text="Close Program",
    font=font_button,
    bg="#dc3545",
    fg=BUTTON_FG,
    relief="flat",
    command=confirm_quit,
    cursor="hand2"
)
btnQuit.pack(side=RIGHT)

# Hover effects
def on_enter(e):
    e.widget['background'] = HOVER_COLOR

def on_leave(e):
    if e.widget == btnQuit:
        e.widget['background'] = "#dc3545"
    else:
        e.widget['background'] = BUTTON_BG

for btn in [btnAdd, btnRemove, btnClear, btnQuit]:
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

# Bind Enter key to addItem function
root.bind('<Return>', lambda event: addItem())

root.mainloop()