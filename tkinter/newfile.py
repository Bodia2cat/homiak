from tkinter import *
import time
root = Tk()
root.title("tkClock")
time1 = ""
time3 = "00:30:00"
clock = Label(root, font=('bold', 20, 'bold'), bg='white')
clock.pack(fill=BOTH, expand=1)
def tick():
        global time1
        global time3
        # узнаем время 
        time2 = time.strftime('%H:%M:%S') 
        # фрейм обновляется как только время меняется
        if time2 != time1:
            time1 = time2
            clock.config(text=time2)
            # вызовы идут каждые 200 милисекунд
        if time3 == time2:
        	clock.config(text="ok")
        	exit()
        clock.after(200, tick)
tick()
root.mainloop()