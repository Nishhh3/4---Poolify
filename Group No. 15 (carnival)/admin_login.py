import customtkinter as ctk
import tkinter as tr
from tkinter import messagebox as mb
window = ctk.CTk()
window.title("ACCESS")
window.geometry('340x340')
window.configure(fg_color='#3B0909',borderwidth=5)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

desired_width = 340
desired_height = 400
center_window(window, desired_width, desired_height)

def login():
    passcode = passcode_entry.get()


    if(passcode == ""):
        mb.showerror(title="Invalid credentials",message="Please Enter Correct credentials")
    elif(passcode == 'admin'):
        mb.showinfo(title="SUCCESS", message="WELCOME ADMIN !!!")
        window.destroy()
        import admin
    else:
        mb.showerror(title="FAILED", message="wrong passcode")


frame = tr.Frame(bg='#fac6c6')

login_label = ctk.CTkLabel(window,text='ADMIN ACCESS',bg_color='#3B0909',font=("Times", 35),text_color='#DACACA')
passcode_label = ctk.CTkLabel(window,text='PASSCODE',bg_color='#3B0909',font=('Arial',20),text_color='#DACACA')
passcode_entry = ctk.CTkEntry(window,font=('Arial',20),width=80,height=36,fg_color='#DACACA',show='*',text_color='#3B0909')
login_btn = ctk.CTkButton(window,text='LOGIN',fg_color="#FFE8E8",corner_radius=50,width=100,text_color='black',
                          font=('times',20,'bold'),border_width=3,border_color='grey',hover_color='white',
                          command= login)
ctk.CTkLabel(window,text='- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -',
             bg_color='#3B0909',fg_color='#3B0909').place(x=0,y=50)
login_label.place(x=30,y=10)
passcode_label.place(x=30,y=130)
passcode_entry.place(x= 170,y=125)

login_btn.place(x=120,y=200)

frame.pack()


window.mainloop()




