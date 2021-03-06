from tkinter import *

from groot import input_taking
from speechtotext import listen


window = Tk()
button_flag = True
#this is to set window title
window.title("I'm Groot")

#set background colour
window.configure(background="#D7DBDD")

#this funtion is to remove output evertime
def removeoutput():
    global ans, i
    if i>1:
        blank.delete(0, END)
        blank.insert(0, ans)

    else:
        blank.insert(0, ans)
    i+=1

#this funtion is to do things on press enter
def OnClicked(arg=None):
    global ans
    userData = E1.get()
    ans=input_taking(userData)
    E1.delete(0,END)
    removeoutput()
    return userData

#this funtion is to do things on press speak
def listen_def():
    global ans
    textfromspeach=listen();
    ans=input_taking(textfromspeach)
    removeoutput()


#text input
label1 = Label(window,text="Enter text here:-",width=15)
label1.grid(row=0, sticky=W)
E1 = Entry(window, width=60)
E1.grid(row=0,column=1)
E1.focus_set()
E1.bind("<Return>",OnClicked)
i=1
#listen button
my_text = Label(window, text="Output:-", width=10)
my_text.grid(row=1)
blank = Entry(window, text="s", width=60)
blank.grid(row=1, column=1)


#text2=Label(window,text="")
photo=PhotoImage(file="./asset/img/icon2.ppm")
L1 = Button(window,text="Press to speak",image=photo, command=listen_def,width = 26, height=50)
L1.grid(row=0, column=2, columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)

#this is to make window on top
#not able to get it in focus have something is mind please help ;)
window.attributes("-topmost", True)

#this is set window default size and its position
window.geometry("750x66+700+400")

window.mainloop()
