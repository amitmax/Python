from tkinter import *
from tkinter import messagebox 
from tkinter import filedialog

root = Tk()
root.geometry("520x600")
root.title("Notepad")
root.resizable(False,False)
root.config(bg="lightblue")

def save_file():
    open_file = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
    if open_file is None:
        return
    text = str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()
    messagebox.showinfo("Saved","Your file as been saved")
    entry.delete(1.0,END)


def open_file():
    file = filedialog.askopenfile(mode="r",filetypes=[("text files","*.txt")])
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content)
    messagebox.WARNING("Opened","Your file as been Opened")


def reset_text():
    entry.delete(1.0,END)
    pass



SF = Button(root,width=20,height=2,bg="#fff",text="Save File",command=save_file).place(x=20,y=10)
OF = Button(root,width=20,height=2,bg="#fff",text="Open File",command=open_file).place(x=180,y=10)
RT = Button(root,width=20,height=2,bg="#fff",text="Reset File",command=reset_text).place(x=340,y=10)

entry = Text(root,height=22,width=50,wrap=WORD,font="Calibri")
entry.config(highlightthickness=1,highlightcolor="Black")
entry.place(x=10,y=60)

root.mainloop()