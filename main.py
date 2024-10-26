import tkinter
from tkinter import *

root = Tk ()
root.title ( "To do List" )
root.geometry ("400x650+400+100")
root.resizable( False,False )

#Background Color
root.configure (bg = 'Black')

task_list = []

#Icon
Image_icon = PhotoImage( file="Resources/Icon.png" )
root.iconphoto ( False, Image_icon )

#Top Bar
TopImage = PhotoImage( file="Resources/TopBar.png" )
Label (root, image=TopImage ).pack()

#Main
frame = Frame( root, width=400, height=50, bg= "white" )
frame.place( x=0, y=180 )

#Input
task = StringVar()
task_entry = Entry( frame, width=18, font=("Poppins", 10, "bold"), bd=0)
task_entry.place( x=10, y=7 )

#Buttons

#Add Button
button = Button (frame, text= "ADD", font=("Poppins", 20, "bold") , width= 6, bg= "black", fg= "#fff", bd=0 )
button.place (x=300, y=0 )

#To-do List
frame1 = Frame (root, bd=3, width=700, height=280, bg="black")
frame1.pack (pady= (160, 0))

#ListBox
listbox = Listbox (frame1, font=("Poppins", 12, "bold"), width= 40, height= 16, bg= "black", fg= "white", cursor= "hand2", selectbackground= "red") 
listbox.pack (side=LEFT, fill=BOTH, padx= 2)

#ScrollBar
scrollbar = Scrollbar (frame1)
scrollbar.pack (side= RIGHT, fill= BOTH)

listbox.config (yscrollcommand= scrollbar.set)
scrollbar.config (command=listbox.yview)

#Delete


root.mainloop()