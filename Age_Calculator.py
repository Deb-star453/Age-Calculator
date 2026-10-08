import tkinter as tk
from datetime import date
root=tk.Tk()
def calculating_age(): 
    year=int(entry1.get())
    month=int(entry2.get())
    day=int(entry3.get())
    birthday=date(year,month,day)
    today=date.today()
    years=today.year-birthday.year
    if (today.month,today.day)<(birthday.month,birthday.day): 
        years=years-1
    last_birthday=date(today.year,birthday.month,birthday.day)
    if last_birthday>today: 
        last_birthday=date(today.year-1,birthday.month,birthday.day)
    days=(today-last_birthday).days
    label2.config(text="Your age is: "+str(years)+"years and "+str(days)+"days")
root.title("Age Calculator")
root.geometry("500x500")
heading=tk.Label(root,text="AGE CALCULATOR",font=("Arial",22))
heading.pack(pady=17)
label1=tk.Label(root,text="Enter your date of birth(year/month/date)",font=("Arial",15))
label1.pack(pady=12)
entry1=tk.Entry(root)
entry1.pack(pady=7)
entry2=tk.Entry(root)
entry2.pack(pady=5)
entry3=tk.Entry(root)
entry3.pack(pady=5)
button=tk.Button(root,text="Calculate Age",command=calculating_age)
button.pack(pady=10)
label2=tk.Label(root,text="")
label2.pack(pady=10)
root.mainloop()
