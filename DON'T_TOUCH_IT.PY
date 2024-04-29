from tkinter import*
from find_motion import find_motion


gauru = Tk()
gauru.title("ICODEEE")
gauru.geometry("400x300")


menubar = Menu(gauru)
  
# Adding File Menu and commands
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='File', menu = file)
file.add_command(label ='New File', command = None)
file.add_command(label ='Open...', command = None)
file.add_command(label ='Save', command = None)
file.add_separator()
file.add_command(label ='Exit', command = gauru.destroy)
  
# Adding Edit Menu and commands
edit = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Edit', menu = edit)
edit.add_command(label ='Cut', command = None)
edit.add_command(label ='Copy', command = None)
edit.add_command(label ='Paste', command = None)
edit.add_command(label ='Select All', command = None)
edit.add_separator()
edit.add_command(label ='Find...', command = None)
edit.add_command(label ='Find again', command = None)
  
# Adding Help Menu
help_ = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label =' Swag 7 Stars', command = None)
help_.add_command(label =' Contact Us ', command = None)
help_.add_separator()
help_.add_command(label =' S7S ', command = None)
  
# display Menu
gauru.config(menu = menubar)

#label
label = Label(gauru,font=('Helvetica',35, 'bold'),foreground="deepskyblue" ,text="  ")
label.grid(sticky=N)

#button main
button1 = Button(gauru, text=" Start Detection ",fg="white", height=3, width=13, command=find_motion, bg="deepskyblue" ,font=('Helvetica',15, 'bold'))
button1.grid(row=1, pady=(25,10),padx=(20,0), column = 0)


#exit button
button2 = Button(gauru, text="exit",fg="deepskyblue", bg="white", height=3, width=13, command=gauru.quit,font=('Helvetica',15, 'bold'))
button2.grid(row=1, pady=(25,10),padx=(20),column=1)


##footer
label2 = Label(gauru, text=" welcome",font=('Helvetica',20, 'bold'),fg="deepskyblue")
label2.grid(row=2, columnspan = 3)


gauru.mainloop()
