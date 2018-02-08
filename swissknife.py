#import Tkinter
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import ttk

###### constants
apostrophe="'"
comma=","
o_parethesis="("
c_parethesis=")"
###############

def e1_callback(event):
    #this select all the text
    event.widget.tag_add("sel","1.0","end")

def list_creation(contents,f_apostrophe,f_comma):

    newcontens=""

    if f_apostrophe == 0:
        apo_yn=""
    else:
        apo_yn=apostrophe

    if f_comma == 0:
        comma_yn=""
    else:
        comma_yn=comma


    for line in contents.split():
            newcontens=newcontens+apo_yn+line+apo_yn+comma_yn

    if len(newcontens) > 0:
        len_contents=int(len(newcontens)-1)
        newcontens=o_parethesis+newcontens[0:len_contents]+c_parethesis
    else:
        newcontens=""

    return newcontens

def gui_insert_list(contents):
    entry1.delete(1.0, 1000.0)
    entry1.insert(1.0,contents)

def submit():
    contents=entry.get(1.0, 1000.0)
    print(contents.splitlines())
    gui_insert_list(list_creation(contents,f_apostrophe_check.get(),f_comma_check.get()))



#GUI design
root = Tk()

########################### TAB creation ############################
#FIRST
tabControl = ttk.Notebook(root)          # Create Tab Control
tab1 = Frame(tabControl)            # Create a tab
tabControl.add(tab1, text='Sql list creation')      # Add the tab
#SECOND
tab2 = Frame(tabControl)            # Create a tab
tabControl.add(tab2, text='Lists comparison')      # Add the tab
tabControl.pack()  # Pack to make visible
#####################################################################


############################### FILL TAB1  ##########################
# first scrolledtext
entry = ScrolledText(tab1,width=70,height=10)
entry.bind('<Control-KeyRelease-a>', e1_callback)
entry.pack(padx=0,pady=20,ipady=70)
# second scrolledtext
entry1= ScrolledText(tab1,width=70,height=10)
entry1.bind('<Control-KeyRelease-a>', e1_callback)
entry1.pack(padx=10,pady=20,ipady=10)


f_apostrophe_check = IntVar()
f_apostrophe_check.set(1)
chk = Checkbutton(tab1,text='Apostrophe?', variable=f_apostrophe_check)
chk.pack(side=LEFT)

f_comma_check = IntVar()
f_comma_check.set(1)
chk = Checkbutton(tab1,text='Comma?', variable=f_comma_check)
chk.pack(side=LEFT)

button = Button(tab1,text='submit',command=submit)
button.pack()
#####################################################################

############################### FILL TAB2  ##########################
# first scrolledtext
l_l1 = Label(tab2, text="List 1")
l_l1.pack(side="left")
entry_t2_1 = ScrolledText(tab2,width=35,height=10)
entry_t2_1.bind('<Control-KeyRelease-a>', e1_callback)
entry_t2_1.pack(side="left",padx=10,pady=20,ipady=10)
# second scrolledtext
l_l2 = Label(tab2, text="List 2")
l_l2.pack(side="left")
entry_t2_2 = ScrolledText(tab2,width=35,height=10)
entry_t2_2.bind('<Control-KeyRelease-a>', e1_callback)
entry_t2_2.pack(side="right",padx=10,pady=20,ipady=10)

#####################################################################




root.mainloop()
