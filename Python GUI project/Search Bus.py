from tkinter import *
import tkinter as tk
import tkinter as ttk
from tkinter import Entry,Tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser

root = Tk()
root.geometry("300x600")#widthxheight
root.configure(bg="white")
root.title("MSRTC Mobile Reservation")
root.minsize(300,600)#width,height
root.maxsize(300,600)
    
#All icons used
img1 = ImageTk.PhotoImage(Image.open("images/screen.png").resize((300, 74)))
Top = Label(image=img1, bg="white").place(x=0,y=0)

img2 = ImageTk.PhotoImage(Image.open("images/search icon.png").resize((20, 20)))
search_icon = Label(image=img2, bg="white").place(x=85,y=80)

img3 = ImageTk.PhotoImage(Image.open("images/destination.png").resize((25, 25)))
source_icon = Label(image=img3, bg="white").place(x=5,y=145)
destination_icon = Label(image=img3, bg="white").place(x=5,y=210)

img4 = ImageTk.PhotoImage(Image.open("images/calendar.png").resize((20, 25)))
date_icon = Label(image=img4, bg="white").place(x=7,y=273)

img5 = ImageTk.PhotoImage(Image.open("images/bus_icon.png").resize((20, 20)))
date_icon = Label(image=img5, bg="white").place(x=7,y=343)

img6 = ImageTk.PhotoImage(Image.open("images/option.png").resize((20,20)))
#option_icon = Button(image=img6,bg="#b452ff").place(x=6,y=7)

img7 = ImageTk.PhotoImage(Image.open("images/msrtc.png").resize((18,15)))
option_icon = Label(image=img7).place(x=35,y=10)

def map():
   url="https://www.google.com/maps"
   webbrowser.open_new_tab(url)

img8 = ImageTk.PhotoImage(Image.open("images/map.png").resize((20,16)))
map_icon = Button(image=img8,bg="#b452ff",borderwidth=0,command=map).place(x=265,y=12)

#All labels
heading = Label(root, text="MSRTC Mobile Reservation",bg="#b452ff", fg="white",font=("calibri",13,"bold")).place(x=60, y=7)
search_bus = Label(root, text="Search Bus", bg="White",font=('calibri',12,'bold')).place(x=115, y= 80)
source_input = Label(root, text="Source/पासून",bg="White", font=('calibri',11)).place(x=40, y= 120)
destination_input = Label(root, text="Destination/पर्यंत",bg="White", font=('calibri',11)).place(x=40, y= 185)
date_input = Label(root, text="Date of Journey",bg="White", font=('calibri',11)).place(x=40, y= 250)
Bus_input = Label(root, text="Bus Type",bg="White", font=('calibri',11)).place(x=40, y= 315)

#All textbox
source = Text(root, height = 1, pady=3,width = 30,bg = "white",font=('calibri',12),cursor='xterm').place(x=35, y=145) 
destination = Text(root, height = 1, pady=3,width = 30,bg = "white",font=('calibri',12),cursor='xterm').place(x=35, y=210)
date = Text(root, height = 1, pady=3,width = 30,bg = "white",font=('calibri',12),cursor='xterm').place(x=35, y=275)

Bus_type = Entry(root,cursor='hand2',bg = "white",font=('calibri',12))
Bus_type.insert(0,"ALL")
Bus_type.place(x=35, y=340, width=250, height=30) 

def Note():
    messagebox.showinfo("Redirected", "No bus services for now!")
    messagebox.place(x=65,y=450)
    
#The Search Button
Search_button=Button(root, text="Search Bus/बस सेवा", height=1, width=18, fg='white', bg='#ff6600',font=('calibri',11,'bold'),borderwidth=3, relief=RIDGE,command=Note)
Search_button.place(x=80,y=400)

#sidebar execution
sidebar=Frame(root, height = 573, width=198, bg="white", highlightthickness=1,highlightbackground="#ff6600")

img9 = ImageTk.PhotoImage(Image.open("images/logo.png").resize((200,100)))
logo = Label(sidebar,image=img9,bg="#b452ff",borderwidth=0).place(x=0,y=0)

img10 = ImageTk.PhotoImage(Image.open("images/options_page.png").resize((195,198)))
option_page = Label(sidebar,image=img10,bg="#b452ff",borderwidth=0).place(x=1,y=100)

sidebar.lift()

def side_bar():
   if(sidebar.winfo_ismapped()==True):
      sidebar.place_forget()
   else: sidebar.place(x=0,y=48)

option=Button(root,image=img6,borderwidth = 0,bg= "#b452ff",command=side_bar).place(x=6,y=7)

root.mainloop()