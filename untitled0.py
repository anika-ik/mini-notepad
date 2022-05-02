from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

root= Tk()
root.minsize(650,650)
root.maxsize(650,650)

label= Label(root, text="File name")
label.place(relx= 0.3, rely=0.03, anchor=CENTER)

input_box= Entry(root)
input_box.place(relx= 0.45, rely= 0.03, anchor= CENTER)

open_img= ImageTk.PhotoImage(Image.open("open.png"))
save_img= ImageTk.PhotoImage(Image.open("save.png"))
exit_img= ImageTk.PhotoImage(Image.open("exit.jpg"))

text= Text(root, height= 35, width= 80 )
text.place(relx= 0.5, rely=0.5, anchor= CENTER)

name= ""
def openfile():
    global name
    text.delete(1.0, END)
    input_box.delete(0, END)
    text_file= filedialog.askopenfilename(title= "open text file", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    name= os.path.basename(text_file)
    formated_name= name.split('.')[0]
    input_box.insert(END, formated_name)
    root.title(formated_name)
    text_file= open(name,'r')
    paragraph= text_file.read()
    text.insert(END, paragraph)
    text_file.close()
    
    
open_btn= Button(root, image= open_img, text= "open file", command= openfile)
open_btn.place(relx= 0.05, rely= 0.03, anchor= CENTER)

save_btn= Button(root, image= save_img, text= "save file")
save_btn.place(relx= 0.10, rely= 0.03, anchor= CENTER)

exit_btn= Button(root, image= exit_img, text= "exit file")
exit_btn.place(relx= 0.15, rely= 0.03, anchor= CENTER)

root.mainloop()