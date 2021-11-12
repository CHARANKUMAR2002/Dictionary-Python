from tkinter import *
import PyDictionary as dic

d = Tk()
w =1000
h =600
sw = d.winfo_screenwidth()
sh = d.winfo_screenheight()
x = (sw/2)-(w/2)
y = (sh/2)-(h/2)
d.geometry("%dx%d+%d+%d" % (w,  h, x, y))
d.resizable(0,0)
d.config(bg='black')
d.title("Dictionary")
d.attributes("-toolwindow", True)
title = Label(d, text="Dictionary", bg='black', fg='white', font=('rosemary', 30, 'bold', 'italic'))
title.pack(pady=10, fill=X)
Label(d, text="Enter The Word Here : ", bg='black', fg='white', font=('arial', 15, 'bold', 'italic')).place(x=10, y=90)
word = Entry(d, bg='black', fg='white', font=('arial', 15, 'italic'), width=25, border=0.5)
word.place(x=230, y=92)
meaning_box = Text(d, height=18, width=85, border=0, bg='black', fg='white', font=('arial', 15, 'bold'))
meaning_box.place(x=25, y=140)

def meaning():
    mean = word.get()
    m=str(mean)
    Meaning = dic.PyDictionary(m)
    M = Meaning.getMeanings()
    a = Meaning.getAntonyms()
    s = Meaning.getSynonyms()
    Mean = "\nMeaning", M ,"\n_____________________________________________________________________________________" ,"\n Antonyms", a,"\n_____________________________________________________________________________________", "\n Synonyms",s
    meaning_box.insert(0.0, Mean)


def close():
    d.destroy()


def clear_fields():
    word.delete(0, END)
    meaning_box.delete(0.0, END)


Button(d, text="Find Meaning", border=0, command=meaning, font=('rosemary', 12, 'italic'), bg='black', fg='white', activebackground='black', activeforeground='white',)\
    .place(x=550, y=90)
Button(d, text="Clear All", border=0, command=clear_fields, font=('times', 12,'bold', 'italic'), bg='black', fg='white', activebackground='black', activeforeground='white')\
    .place(x=680, y=90)
Button(d, text="Close", border=0, command=close, font=('times', 12,'bold', 'italic'), bg='black', fg='white', activebackground='black', activeforeground='white')\
    .place(x=780, y=90)

d.mainloop()