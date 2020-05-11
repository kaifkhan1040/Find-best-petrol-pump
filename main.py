from tkinter import *
import petrol_pump1
root=Tk()
root.title('PETROL PUMP RUNUP')
def quit():
    root.destroy()
def f():
    quit()
    petrol_pump1.pump()
root.geometry('350x300+120+120')
root.title('Petrol Pump')
l1=Label(root,text="Finder the best Petrol Pump in your city .").grid(row=0,column=1)
btn=Button(root,text='Start Finding',command=f).grid(row=1,column=1)
btn1=Button(root,text='QUIT',command=quit).grid(row=2,column=1)
root.mainloop()