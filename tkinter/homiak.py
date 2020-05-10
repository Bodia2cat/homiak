from tkinter import *
import time
import os
root = Tk()
#clock function
time1 = ""
time_deaf_2 = "10:40:00"
time_deaf_1 = "18:00:00"
clock = Label(root, font=('bold', 20, 'bold'), bg='white')
clock.pack()
def tick():
	global time1
	global time3
	# узнаем время 
	time2 = time.strftime('%H:%M:%S') 
	if time3 == time2 or time4 == time2 or time_deaf_1 == time2 or time_deaf_2 == time2:
		import pyglet
		song = pyglet.media.load('htc_basic.mp3')
		song.play()
		pyglet.app.run()
		exit()
	clock.after(200, tick)
    
def cllock():
        global time1
        global time3
        # узнаем время 
        time2 = time.strftime('%H:%M:%S') 
        # фрейм обновляется как только время меняется
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
            # вызовы идут каждые 200 милисекунд
        clock.after(200, cllock)

cllock()

#Clean s

t_m = "Да, в 14:00"
t_t = "Нет"
t_w = "Нет"
t_th = "Да, в 14:00"
t_f = "Нет"
t_s = "Нет"
t_san = "Да, в 11-12"

#----------------------#

#-------------------------

root.title("Таблица рационна хомяка по дням")
#text to insert to clean window
def M_c(event):
	text.delete(1.0, END)
	text.insert(1.0, t_m)
def T_c(event):
	text.delete(1.0, END)
	text.insert(1.0, t_t)
def W_c(event):
	text.delete(1.0, END)
	text.insert(1.0, t_w)
def Th_c(event):
	text.delete(1.0, END)
	text.insert(1.0, t_th)
def F_c(event):
	text.delete(1.0, END)
	text.insert(1.0, t_f)
def S_c(event):
	text.delete(1.0, END)
	text.insert(1.0, t_s)
def San_c(event):
	text.delete(1.0, END)
	text.insert(1.0, t_san)
def Clean_window(event):
	a = Toplevel(root)
	#window title
	a.title("Разписание уборки")
	#buttons
	q1 = Button(a, text="Понедельник")
	q2 = Button(a, text="Вторник")
	q3 = Button(a, text="Среда")
	q4 = Button(a, text="Четверг")
	q5 = Button(a, text="Пятница")
	q6 = Button(a, text="Субота")
	q7 = Button(a, text="Воскресенье")
	#bind
	q1.bind("<Button-1>", M_c)
	q2.bind("<Button-1>", T_c)
	q3.bind("<Button-1>", W_c)
	q4.bind("<Button-1>", Th_c)
	q5.bind("<Button-1>", F_c)
	q6.bind("<Button-1>", S_c)
	q7.bind("<Button-1>", San_c)
	#pack
	q1.pack()
	q2.pack()
	q3.pack()
	q4.pack()
	q5.pack()
	q6.pack()
	q7.pack()
    #--------------------------------#
def clock_option(event):
	c_o = Toplevel(root)
	l_c = Label(c_o, text="Первое время:")
	e_c = Entry(c_o)
	l_c_2 = Label(c_o, text="Второе время:")
	e_c_1 = Entry(c_o)
	b_c = Button(c_o, text = "Готово")

	def c_logic(event):
		time3 = e_c.get()
		time4 = e_c_1.get()
		print(time3)
		print(time4)
	b_c.bind("<Button-1>", c_logic)


	l_c.pack()
	e_c.pack()
	e_c.pack()
	l_c_2.pack()
	e_c_1.pack()
	b_c.pack()
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
b_clock = Button(text="Запустить таймер для кормежки")
b1 = Button(text="Понедельник")
b2 = Button(text="Вторник")
b3 = Button(text="Среда")
b4 = Button(text="Четверг")
b5 = Button(text="Пятница")
b6 = Button(text="Суббота")
b7 = Button(text="Воскресенье")
b_clean = Button(text="Расписание уборки")
b_clock_o = Button(text="Настройки таймера")
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
b_clean.bind("<Button-1>", Clean_window)
b_clock.config(command=tick)
b_clock_o.bind("<Button-1>", clock_option)

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
b_clean.pack()
b_clock.pack()
b_clock_o.pack(side='right', anchor='n')
text.pack(side='bottom', anchor='s')
#loop
root.mainloop()
