#Hamzah Ahmed
#v1.0
#Research in IT

from tkinter import *
from tkinter import ttk
import tkinter
import os
from tkinter import messagebox
import time

def submit():
    try:

        #Takes all codes in avaiablecodes and makes it into a list
        file = open("availablecodes.txt", "r")
        lines = file.readlines()
        new_lines=[]
        for x in lines:
            new_lines.append(x.strip("\n"))
        file.close()

        cde = code.get() #Gets code user entered

        #If a blank entry was entered, tells user incorrect pin
        if cde=="":
            messagebox.showinfo("Error", "Invalid pin!")

        #If code is in the list of generated codes, opens the door and tells user success
        elif str(cde) in new_lines:
            # RUN SERVO TEST2 PY PROGRAM HERE!!!!!!!!!
            code.set("")
            os.system("python open.py")

            #Records time and code used to enter the door
            with open("entrylog.txt", "a") as file:
                file.write("Code, " + str(cde) + ", was used at " + time.ctime() + "\n")
            messagebox.showinfo("Success", "You are authorized to enter!")
        else:
            messagebox.showinfo("Error", "Invalid pin!")

    #Didn't enter the right pin, then tells user invalid pin
    except:
        messagebox.showinfo("Error", "Invalid pin!")


root = Tk()
root.title("Security Door Access Point")
root.attributes('-fullscreen', True) #Makes screen fullscreen
code=StringVar()
style = ttk.Style()

mainframe = tkinter.Frame(root,width=1024,height=600)
mainframe.grid(column=0, row=0, sticky=(N, W))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
content = ttk.Frame(root, padding=(1,1,1,1))
frame = tkinter.Frame(content, borderwidth=5, relief="sunken", bg="firebrick3",width=1300, height=800)
code_entrylbl = Label(content, text="ENTER CODE HERE", bg="firebrick3")
code_entry = ttk.Entry(content, width=30, textvariable=code,font=("Courier", 22))
code_entrylbl.config(width=20)
code_entrylbl.config(font=("Courier", 32))

content.grid(column=0, row=0, sticky=(W))
enter_button=tkinter.Button(content,font=("Courier", 22), text="ENTER",bg="light blue",width=20,command=submit).grid(column=0,row=2,sticky=(N))
frame.grid(column=0, row=0, rowspan=3, sticky=(W))
code_entrylbl.grid(column=0, row=0, sticky=(S), padx=1)
code_entry.grid(column=0, row=1, sticky=(N), pady=1, padx=1)


#Only allows 4 characters to be entered
def character_limit(entry_text):
    if len(entry_text.get()) > 0:
        code.set(code.get()[:4])
code.trace("w", lambda *args: character_limit(code))


code_entry.focus()

root.mainloop()