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

img2 = ImageTk.PhotoImage(Image.open("images/option.png").resize((20,20)))

img3 = ImageTk.PhotoImage(Image.open("images/msrtc.png").resize((18,15)))
option_icon = Label(image=img3).place(x=35,y=10)

def map():
   url="https://www.google.com/maps"
   webbrowser.open_new_tab(url)

img4 = ImageTk.PhotoImage(Image.open("images/map.png").resize((20,16)))
map_icon = Button(image=img4,bg="#b452ff",borderwidth=0,command=map).place(x=265,y=12)

#All labels
heading = Label(root, text="MSRTC Mobile Reservation",bg="#b452ff", fg="white",font=("calibri",13,"bold")).place(x=60, y=7)
Login_Head = Label(root, text="LOGIN", bg="White",font=('calibri',12,'bold')).place(x=130, y= 80)
Email_input = Label(root, text="Email",bg="White", font=('calibri',11)).place(x=40, y= 120)
Password_input = Label(root, text="Password",bg="White", font=('calibri',11)).place(x=40, y= 185)
forgot = Label(root, text="Forgot Password",bg="white",fg="blue",font=('ca;ibri',8,'underline')).place(x=180, y=245)

#All textbox
Email = Text(root, height = 1, pady=3,width = 30,bg = "white",font=('calibri',12),cursor='xterm').place(x=35, y=145) 
Password = Text(root, height = 1, pady=3,width = 30,bg = "white",font=('calibri',12),cursor='xterm').place(x=35, y=210)


#The Login Button
def Note():
    messagebox.showinfo("Message", "Login Successful!")
    
Login_Button=Button(root, text="Login", height=1, width=12, fg='white', bg='#ff6600',font=('calibri',11,'bold'),borderwidth=3, relief=RIDGE,command=Note)
Login_Button.place(x=100,y=275)



img7 = ImageTk.PhotoImage(Image.open("images/OR.png").resize((300,55)))
OR_image = Label(root, image=img7,borderwidth=0).place(x=0,y=330)

img8 = ImageTk.PhotoImage(Image.open("images/google.png").resize((50,50)))
google_image = Label(root,image=img8,borderwidth=0,bg="white").place(x=50,y=400)

img9 = ImageTk.PhotoImage(Image.open("images/facebook.png").resize((50,50)))
facebook_image = Label(root,image=img9,borderwidth=0,bg="white").place(x=125,y=400)

img10 = ImageTk.PhotoImage(Image.open("images/twitter.png").resize((50,50)))
twitter_image = Label(root,image=img10,borderwidth=0,bg="white").place(x=200,y=400)

label1 = Label(text="Not Registered Yet?",font=('calibri',9),bg="white").place(x=95,y=475)
label2 = Label(text="Sign Up",font=('calibri',9,'underline'),fg="blue",bg="white").place(x=125,y=495)

#sidebar execution
sidebar=Frame(root, height = 573, width=198, bg="white", highlightthickness=1,highlightbackground="#ff6600")

img5 = ImageTk.PhotoImage(Image.open("images/logo.png").resize((200,100)))
logo = Label(sidebar,image=img5,bg="#b452ff",borderwidth=0).place(x=0,y=0)

img6 = ImageTk.PhotoImage(Image.open("images/options_page.png").resize((195,198)))
logo = Label(sidebar,image=img6,bg="#b452ff",borderwidth=0).place(x=1,y=100)

sidebar.lift()

def side_bar():
   if(sidebar.winfo_ismapped()==True):
      sidebar.place_forget()
   else: sidebar.place(x=0,y=48)

#option Button
option=Button(root,image=img2,borderwidth = 0,bg= "#b452ff",command=side_bar).place(x=6,y=7)

root.mainloop()