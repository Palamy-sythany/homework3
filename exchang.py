import tkinter as tk
from functools import  partial
root=tk.Tk()
root.title("Exchange")
root.geometry('500x350')
def Exchange():
    b=int(bath.get())
    r=int(rate.get())
    k=b*r
    kip.set(str(k))
def Allclear():
    bath.set('')
    kip.set('')

bath=tk.StringVar()
kip=tk.StringVar()
rate=tk.StringVar()

l0=tk.Label(root,font=('Sysettha OT',16),fg='red',text="ໂປຮແກຮມແລກປຽນເງີນບາດເປັນກີບ").place(x=150,y=10)
l1=tk.Label(root,font=('Sysettha OT',12),fg='red',text="ປອນຈຳນວນເງີນ").place(x=50,y=60)
l2=tk.Label(root,font=('Sysettha OT',12),fg='red',text="ປອນອັດຕາແລກປຽນ").place(x=50,y=120)
l3=tk.Label(root,font=('Sysettha OT',12),fg='red',text="ຈຳນວນເງິນທີ່ໄດ້:").place(x=50,y=180)

t1=tk.Entry(root,font=('Sysettha OT',12),fg='black',textvariable=bath).place(x=200,y=60)
t2=tk.Entry(root,font=('Sysettha OT',12),fg='black',textvariable=rate).place(x=200,y=120)
t3=tk.Entry(root,font=('Sysettha OT',12),fg='black',textvariable=kip).place(x=200,y=180)
b1=tk.Button(root,font=('Sysettha OT',12),fg='black',text="ແລກປ່ຽນ",width=10,height=1,command=Exchange).place(x=150,y=250)
b2=tk.Button(root,font=('Sysettha OT',12),fg='black',text="ລ້າງ",width=10,height=1,command=Allclear).place(x=300,y=250)

root.mainloop()