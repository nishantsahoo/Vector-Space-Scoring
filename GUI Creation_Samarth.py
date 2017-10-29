from tkinter import *
import math

root = Tk()
root.geometry("800x400")

# Heading
w = Label(root, text="VECTOR SPACE MODEL CALCULATOR",
                fg="blue",
                font=("Franklic Gothic Book", 24),
                justify= CENTER, height=2)
w.pack()

# Taking Input
Label(root, text="Enter Query",
            font=("Franklic Gothic Book", 16),
            justify= CENTER, height=2).pack()
        

# Storing into a variable s on click of a button fetch
def fetch():
    print ('Input =>',e.get())
    s=''
    s=e.get()
    print(s)
# Data is fetched into s
    
e=Entry(root, width=40)
e.pack(ipady=5)

e.focus()                                    
e.bind('<Return>', (lambda event: fetch()))  
btn = Button(root, text='Fetch', command=fetch, height=1, width=7) 
btn.pack(side=TOP)

# To display the tf-idf value
Label(root, text="Tf-Idf",
            font=("Franklic Gothic Book", 16),
            justify= CENTER, height=2).pack()

# Entry box for input
r = StringVar()     
r_entry = Entry(root, width=40, textvariable=r)
r_entry.pack()

# Output the same variable as entered in the entry box
s = StringVar() 
def comp_s(event):
    global s
    s.set('%g' % float(r.get())) #using this ptting the value of string r into s string

r_entry.bind('<Return>', comp_s)

compute = Label(root, text='=') 
compute.pack()  

s_label = Label(root, textvariable=s, width=18) #the value is output here
s_label.pack()

root.mainloop()
