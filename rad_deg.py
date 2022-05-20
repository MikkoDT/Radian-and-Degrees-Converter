from tkinter import *
import numpy as np

gui = Tk()
gui.title("Rad and Deg Converter")
gui.iconbitmap('Robotmik.ico')
gui.configure(bg='black')

# Rad to Deg converter
RtoD = LabelFrame(gui,text="Rad to Deg Converter",font=(18),fg="white",padx=18,pady=18,bg="green")
#RtoD.pack(padx=20,pady=20)
RtoD.grid(row=0,column=0)
RadI_1 = Entry(RtoD,width=12,font=(24),borderwidth=15)
rad1 = Label(RtoD,text=("rad"),font=(24))

def r_d1():
    T1 = float(RadI_1.get())
    T1 = (T1*180)/np.pi
    DegI_1.delete(0,END)
    DegI_1.insert(0,np.around(T1,3))

To1 = Button(RtoD,text="→",font=(24),bg="red",command=r_d1)
DegI_1 = Entry(RtoD,width=12,font=(24),borderwidth=15)
deg1 = Label(RtoD,text=("deg"),font=(24))

RadI_1.grid(row=0,column=0)
rad1.grid(row=0,column=1)
To1.grid(row=0,column=2)
DegI_1.grid(row=0,column=3)
deg1.grid(row=0,column=4)

# Deg to Rad converter
DtoR = LabelFrame(gui,text="Deg to Rad Converter",font=(18),padx=18,pady=18,bg="yellow")
DtoR.grid(row=1,column=0)
DegI_2 = Entry(DtoR,width=12,font=(24),borderwidth=15)
deg2 = Label(DtoR,text=("deg"),font=(24))

def d_r1():
    T2 = float(DegI_2.get())
    T2 = (T2/180)*np.pi
    RadI_2.delete(0,END)
    RadI_2.insert(0,np.around(T2,3))

To2 = Button(DtoR,text="→",font=(24),bg="blue",command=d_r1)
RadI_2 = Entry(DtoR,width=12,font=(24),borderwidth=15)
rad2 = Label(DtoR,text=("rad"),font=(24))

DegI_2.grid(row=1,column=0)
deg2.grid(row=1,column=1)
To2.grid(row=1,column=2)
RadI_2.grid(row=1,column=4)
rad2.grid(row=1,column=3)

gui.mainloop()
