from tkinter import *
root = Tk()

root.title("Таблица рационна хомяка по дням")


def Sunday(event):
	text.delete(1.0, END)
	Tuesday_r = "Утро: \n1) Морковь(4х / 2) \n3) Корм(для всех если надо) \n4)Трава(ладошь / 2)"
	text.insert(1.0, Tuesday_r)

def Saturday(event):
	text.delete(1.0, END)
	Saturday_r = "Утро: \n1) Морковь(x4 / 2) \n3) Корм(для всех) \n4)Трава(ладошь / 2)"
	text.insert(1.0, Saturday_r)

def Friday(event):
	text.delete(1.0, END)
	Friday_r = "Утро: \n1) Морковь(4х / 2) \n3) Корм(для пацанов) \n4)Трава(ладошь / 2)"
	text.insert(1.0, Friday_r)

def Thursday(event):
	text.delete(1.0, END)
	Thursday_r = "Утро: \n1) Морковь(4х / 2) \n3) Корм(для всех если нужно) \n4)Трава(ладошь)"
	text.insert(1.0, Thursday_r)

def Wendsday(event):
	text.delete(1.0, END)
	Wednesday_r = "Утро: \n1) Морковь(4х / 2) \n2) Корм \n3)Трава(ладошь / 2)"
	text.insert(1.0, Wednesday_r)

def Tuesday(event):
	text.delete(1.0, END)
	Tuesday_r = "Утро: \n1) Морковь(4х / 2) \n3) Корм(для пацанов) \n4)Трава(ладошь / 2)"
	text.insert(1.0, Tuesday_r)
def Monday(event):
	text.delete(1.0, END)
	monday_r = "Утро: \n1) Морковь(4х / 2) \n3) Корм \n4)Трава"
	text.insert(1.0, monday_r)

#objects--------------------------
#Label
l1 = Label(text="Какой день?")
#Entry
e1 = Entry(width=20)	
#buttons
b1 = Button(text="Понедельник")
b2 = Button(text="Вторник")
b3 = Button(text="Среда")
b4 = Button(text="Четверг")
b5 = Button(text="Пятница")
b6 = Button(text="Суббота")
b7 = Button(text="Воскресенье")
#Text
text = Text()
#bind------------------------
b1.bind("<Button-1>", Monday)
b2.bind("<Button-1>", Tuesday)
b3.bind("<Button-1>", Sunday)
b4.bind("<Button-1>", Thursday)
b5.bind("<Button-1>", Friday)
b6.bind("<Button-1>", Saturday)
b7.bind("<Button-1>", Sunday)
#pack------------------
l1.pack(anchor="s")
b1.pack(side='left', anchor="n")
b2.pack(side='left', anchor="n")
b2.pack(side='left', anchor="n")
b3.pack(side='left', anchor="n")
b4.pack(side='left', anchor="n")
b5.pack(side='left', anchor="n")
b6.pack(side='left', anchor="n")
b7.pack(side='left', anchor="n")

text.pack(side='bottom', anchor='s')
#loop
root.mainloop()