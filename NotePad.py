from tkinter import*
from tkinter import filedialog

window=Tk()
window.title("NotePad")
window.geometry('600x600')
window.config(bg='lightblue')
window.resizable(False,False)

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file in None:
        return
    text=str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode='r',filetype=['text file','*.text'])
    if file is not None:
        content=file.read()
        entry.insert(INSERT,content)

button1=Button(window,width='20',height='2',bg='#fff',text='save file',command=save_file).place(x=100,y=5)
button2=Button(window,width='20',height='2',bg='#fff',text='open file',command=open_file).place(x=300,y=5)

entry=Text(window,height='33',width='72',wrap=WORD)
entry.place(x=10,y=60)
window.mainloop()
     
        
