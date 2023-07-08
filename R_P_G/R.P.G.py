# Modules
import string
import random
import os
import time
import base64
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyperclip

# GUI window
R_P_G = Tk()
R_P_G.geometry("480x120")
R_P_G.resizable(False,False)

# Icon in Base64
icon = """iVBORw0KGgoAAAANSUhEUgAAAFQAAABUCAYAAAAcaxDBAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz
AAALEwAACxMBAJqcGAAABSlJREFUeJztnFtoHUUYx39JbG1a0wRbCQpSqrQqWLzV4KUi3vqigvom
llbEJ+uDaB9EfNCCSB9EfDOCRdE8KVTFWlCiKNWHJiJoi63aUBFbNRFjEzU2l+PD5Hh2Nztzdma/
vZw984MPztndmW/mf87OzH4zs+DxeDweVzqKLkCALuA8oAfoBKaBCeDfIgtlS5GCrgbuBm4DBoAN
wPLINQvAj8BXwCfAu8BPOZaxJbgCeBP4G6hZ2gIwjPoh2p4LgbexF1FnXwLX51qDEvEwqk2UEjP4
j32JpU1FZTkL2Iu8kFE7BPTnVKfCOBvYT/Zi1u0HYF0uNTOQVS/fBbwF3Jvw+ingC+Bb1FBpHuhD
9fzXARckzOc7YAswblPYVuB5kv2rPgDuRDUNJjYDg8BMgjw/Rf2glWErqrMwVfoIcKND3uuA95vk
XQOeTVWDEtENjGGu7NDidWl4AvOPdga4LKWPUvAkZjEHkWu3t2MWdb+Qn8JYCfyGub3sFPb5tMFf
Dbha2F+uPIi+YhOowIc0HahOSOf31Qx85sbH6Cu2M0O/m9Df+n8CKzL0nRk9wCzxlfoVNcjPkvc0
vmvAHRn7DiHVpm1BP5YcIvuY5muGc7dk7DuElKCbDOcOCPkw8REwpzlnKps4UoJuMJwbEfJhYgo4
qjm3MQf//yMl6BrN8clFy4MxzfFzc/IPyAm6SnN8Sij/JJzWHO/JsQxiguqCEQtC+SdhXnO8WeBF
FOknl7bH5dfrRs0PddN4Lj9Hc+1y4EoHHy6Y2spgGc4Ap4A/si2OmV5gF2pibJ5sI+952XHgBeAi
QZ0SsR34PUXBy26zwB5ymuh7MefKFWmfoRZfZMbuElQybxsmo+mTm2k+jVFVe0pAvyWMlKBiRdk0
sNZVuLhx6ABqlrFdWQXscE0cJ+hd7mWpDM6L0eIEzWsgXmacNYgTNIu5n1ajF8dxaZygy9KVpTKI
CepJgRdUGC+oMNLB1yOoZYzH0U+atQozUhmNYv90MQs8Qrm26ZQGF0GdnyyqhsQtPwy8bji/knA0
/RfsmoM+GjMC86houw39NIaC/6Biu0npJLx6ehL1rG+F7T/0gSb5bYtcf6lleV4OpJ2wTAtwOJD+
Hcu0awmXfVezBBK9/GGBPCqDhKAttRcza/w4VJgsFgHsIbwhIRpsGUJ1DnX2LlqdA4RXe1wc+NwL
HIzk9xiq3QdYD7wROb8+8PmmmPS3oqaWAe4DHg+ci+qzE7gn8P0oapegEdtOKdrJJNmlEbRnIukn
LdPfHkh7uWXaGuEFuY9aph0lgr/lhcnilv+G8EqSfsL/4hHU1u46JyLpD0bSbwTOX/w8B3weuT64
AuQv1Jr7INeixsKgxqDRUUlw/dXPkfTLgBsC38cI79c/RgLS3vJR/DjU446EoLq1oW2JhKADAnlU
hrhw2yhwjUUeXwNXoV9cuwIV4Kgzjn5xbByraXQqC6jdejasoREcmcFuiXoH4RcbnCbcoSbCJXz3
nK2TdsJF0BqqN+6Lya+tkLjlg0wDHwLf0/pTILtpPJImRlrQKtGDQzDZj0OF8YIK4wXVU3NJFCeo
j8ArnHSIE/RkyoJUgXEcRylxguaxe7jsHHJNGCeobYiriuyTztB2GqNKdor075VawiW4vTC1CtZs
4YYz22i/vUqviChn4CHU82zRFc3DBsnpJYSbcY9AtYKdBO4XU8uCrag3dR1DDXqLFsLV5lAzl/tQ
O61FX5SVZoFsV8r0RdHqYUWPx+PxeDyeKvAfEw7OG7CFJVAAAAAASUVORK5CYII="""

# Icon And Background Color
img= base64.b64decode(icon)
img=PhotoImage(data=icon)
R_P_G.iconphoto('True',img)
R_P_G['background']='#F0E6E6'

# Title
R_P_G.title("R.P.G")

# Variables
len_var = IntVar()
check1 = IntVar()
check2 = IntVar()
check3 = IntVar()
check4 = IntVar()
check5 = IntVar()
view = IntVar()
temppass = ""
lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
unnecessary = ['`','~','(',')',':','}','{','[',']','\'','\"',',','^','\\','/',':',';']
symbols = string.punctuation

# Removing Unnecessary Punctuations
for x in unnecessary:
	symbols = symbols.replace(x,'')

# Function For Lower Case Entries
def lowercase() :
	global temppass
	if check5.get() == 1:
		check5.set(0)
		temppass = ""
	if (check1.get() == 1 and check2.get() == 1 and check3.get() == 1 and check4.get() == 1):
		check1.set(0)
		check2.set(0)
		check3.set(0)
		check4.set(0)
		check5.set(1)
	if check1.get() == 1:
		temppass = temppass + lower
	elif check1.get() == 0:
		temppass = temppass.replace(lower,"")

# Function For Upper Case Entries
def uppercase() :
	global temppass
	if check5.get() == 1:
		check5.set(0)
		temppass = ""
	if (check1.get() == 1 and check2.get() == 1 and check3.get() == 1 and check4.get() == 1):
		check1.set(0)
		check2.set(0)
		check3.set(0)
		check4.set(0)
		check5.set(1)
	if check2.get() == 1:
		temppass = temppass + upper
	elif check2.get() == 0:
		temppass = temppass.replace(upper,"")

# Function For Digit Entries
def digit() :
	global temppass
	if check5.get() == 1:
		check5.set(0)
		temppass = ""
	if (check1.get() == 1 and check2.get() == 1 and check3.get() == 1 and check4.get() == 1):
		check1.set(0)
		check2.set(0)
		check3.set(0)
		check4.set(0)
		check5.set(1)
	if check3.get() == 1:
		temppass = temppass + digits
	elif check3.get() == 0:
		temppass = temppass.replace(digits,"")

# Function For Symbol Entries
def symbol() :
	global temppass
	if check5.get() == 1:
		check5.set(0)
		temppass = ""
	if (check1.get() == 1 and check2.get() == 1 and check3.get() == 1 and check4.get() == 1):
		check1.set(0)
		check2.set(0)
		check3.set(0)
		check4.set(0)
		check5.set(1)
	if check4.get() == 1:
		temppass = temppass + symbols
	elif check4.get() == 0:
		temppass = temppass.replace(symbols,"")

# Function For Defaul
def default() :
	global temppass
	if (check1.get() == 1 or check2.get() == 1 or check3.get() == 1 or check4.get() == 1):
		check1.set(0)
		check2.set(0)
		check3.set(0)
		check4.set(0)
	if check5.get() == 1:
		temppass = temppass + lower + upper + digits + symbols
	elif check5.get() == 0 and check1.get() == 0 and check2.get() == 0 and check3.get() == 0 and check4.get() == 0:
		temppass = ""

# Function To Generate Password
def Gen_Pass():
	global temppass
	Pass_Display.delete(0, END)
	length = len_var.get ()
	word = ""
	if len(temppass) > 0:
		for i in range(0, length):
			word = word + random.choice(temppass)
		return word
	else:
		return "!!!Error!!!"

# Function To Display Password
def generate():
	password = Gen_Pass()
	Pass_Display.insert(0, password)

# File Creation
passcode = os.path.join(r"C:\R.P.G","Pass.txt")
if not os.path.exists(r"C:\R.P.G"):
    os.makedirs(r"C:\R.P.G")
passcode = open(r"C:\R.P.G\Pass.txt","a+")
passcode.close

# Function For Copying And Saving The Password
def Copy_Save():
	# To Copy Password
	random_pass = Pass_Display.get()
	pyperclip.copy(random_pass)
	sno = "0"

	# To Get Local Time
	tim = time.localtime()
	current_time = time.strftime("From %Y/%m/%d At %I:%M:%S %p", tim)

	# To Save The Password
	fsize = os.path.getsize(r"C:\R.P.G\Pass.txt")
	if (fsize == 0):
		passcode = open(r"C:\R.P.G\Pass.txt","a+")
		passcode.write("Sr.No.      	Password        		Time")
		passcode.close
	elif (fsize >= 34):
		with open(r"C:\R.P.G\Pass.txt", 'r') as seq:
			lines = seq.read().splitlines()
			last_line = lines[-1]
			sno = last_line[0]
		seq.close
	else:
		sno = 0
	passcode = open(r"C:\R.P.G\Pass.txt","a+")
	passcode.write(f"\n{int(float(sno))+1}		{random_pass}		{current_time}")
	passcode.close

# Open File In Notepad
logs = r"notepad.exe C:\R.P.G\Pass.txt"

# Function To View The File
def View_Pass():
	fsize = os.path.getsize(r"C:\R.P.G\Pass.txt")
	if fsize == 0:
		messagebox.showwarning("!!!ERROR!!!", "No Password Saved")
	elif fsize > 0:
		os.system(logs)

# Function To Reset The File
def Reset():
	password = open(r"C:\R.P.G\Pass.txt","w+")
	for x in password:
		x.strip()

# Password Label
Random_Password = Label(R_P_G, text="Generated Password")
Random_Password.place(x=10,y=5)

# Password Entery
Pass_Display = Entry(R_P_G,width= 34)
Pass_Display.place(x=125,y=5)

# Length Label
Length_label = Label(R_P_G, text="Password's Length")
Length_label.place(x=10,y=33)

# Copy/Save Button
Copy_button = Button(R_P_G, text="Copy/Save", command=Copy_Save)
Copy_button.place(x=170,y=31)

# Generate Button
Generate_button = Button(R_P_G, text="Generate", command=generate)
Generate_button.place(x=255,y=31)

# View Button
View_button = Button(R_P_G, text="View Passwords", command=View_Pass)
View_button.place(x=110,y=65)

# Reset Button
Reset_button = Button(R_P_G, text="Reset Passwords", command=Reset)
Reset_button.place(x=250,y=65)

# Creater's Label
title = Label(R_P_G, text="Random Password Generator")
title.config(font = ('Terminal',12), foreground = 'red', background = '#F0E6E6')
title.place(x=83,y=98)

# CheckButtons For Customizations
Lower_Button = Checkbutton(R_P_G, text="Lower", onvalue = 1, offvalue = 0,
        variable = check1, command = lowercase).place(x=340,y=7)
Upper_Button = Checkbutton(R_P_G, text="Upper", onvalue = 1, offvalue = 0,
        variable = check2, command = uppercase).place(x=410,y=7)
Digits_Buttons = Checkbutton(R_P_G, text="Digits", onvalue = 1, offvalue = 0,
        variable = check3, command = digit).place(x=340,y=35)
Symbol_Buttons = Checkbutton(R_P_G, text="Symbols", onvalue = 1, offvalue = 0,
        variable = check4, command = symbol).place(x=410,y=35)
Default_Button = Checkbutton(R_P_G, text="Default", onvalue = 1, offvalue = 0,
        variable = check5, command = default).place(x=410,y=65)

# Combo Box for length of your password
length_Button = ttk.Combobox(R_P_G, textvariable=len_var, width = 2)
length_Button['values'] = (6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
				17, 18, 19, 20, 21, 22, 23, 24, 25,
				26, 27, 28, 29, 30, 31, 32)
length_Button.current(2)
length_Button.bind('<<ComboboxSelected>>')
length_Button.place(x=120,y=33)

# GUI
R_P_G.mainloop()
