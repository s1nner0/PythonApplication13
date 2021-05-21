
from tkinter import *
list_ = ["pc1","pc2","pc3","pc4","ROBOT-ANDROID"]
foto_list=["pc1.gif","pc2.gif","pc3.gif","pc4.gif"]
global can, pc
def list_to_txt(event):
    global can, pc
    txt.delete(0.0,END)
    valik=lbox.curselection()
    txt.insert(END,lbox.get(valik[0]))
    print(lbox.get(valik[0]))
    can.delete(ALL)
    pc = PhotoImage(file=foto_list[valik[0]])
    print(foto_list[valik[0]])
    can.create_image(0,0,image=pc,anchor=NW)
    

def txt_to_list(event):
    text=text.get(0.0,END)
    text=text[-2:-1]
    if text--"/n":
        pass
    else:
        foto_list.append(text)
        lbox.config(height=len(foto_list))
        lbox.insert(END,text)
        txt.delete(0.0,END)
        text-""

def opisanie():
    text = txt.get(0.0, END)
    print(list(text))
    if text=="pc1.png\n":
        ttt="i9 10900kf \n rtx 3070 gigabyte \n 32gb DDR4 Crucial Ballisitix 3200 mhz \n 700w Cooler master MWE \n 2000 Euro "
    elif text=="pc2.png\n":
        ttt="i7 10700f \n rtx 3060ti gigabyte \n 32gb DDR4 Crucial Ballisitix 3200 mhz \n 700w Cooler master MWE \n 1500 Euro "
    elif text=="pc3.png\n":
        ttt="i5 10600\n rtx 3060 gigabyte \n 32gb DDR4 Crucial Ballisitix 3200 mhz \n 700w Cooler master MWE \n 800 Euro "
    elif text=="pc4.png\n":
        ttt="i3 10100 \n gtx 1050 ti \n 16gb DDR4 Crucial Ballisitix 3200 mhz \n 550w Cooler master MWE \n 600 Euro "
    opis.config(text=ttt)



win=Tk()
lbox=Listbox(win,width=20,height=len(foto_list),selectmode=SINGLE)
for element in foto_list:
    lbox.insert(END,element)

lbox.grid(row=4, column=5)
lbox.bind("<<ListboxSelect>>",list_to_txt)
txt=Text(win,height=4,width=20,wrap=WORD)
txt.grid(row=2, column=7)
txt.bind("<Return>",txt_to_list)
can=Canvas(win,width=130,height=200,bg="gold")
pc = PhotoImage(file="")#220px-PelobatesFuscus.png
panel = Label(win, image = pc)
panel.grid(column=1, row=2)
foto=PhotoImage(file="pc1.gif")
bt=Button(text='Info', command=opisanie).grid()#, command=op
opis=Label(win, text="", width=50, height=20)
opis.grid(row=2, column=3)
can.grid(row=1, column=1)
win.mainloop()
