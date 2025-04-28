import customtkinter as ctk
import tkinter as tr
from tkinter import messagebox as mb
import mysql.connector
window = ctk.CTk()
window.title("ENROLL")
window.geometry('340x400')
window.configure(fg_color='#d1d5fd',borderwidth=5)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

desired_width = 340
desired_height = 400
center_window(window, desired_width, desired_height)
vol_name =''

def reset():
    username_entry.delete(0, ctk.END)
    pass_entry.delete(0, ctk.END)
def toggle_password():
    if pass_entry.cget('show') == '*':
        hide_btn.configure(text_color='dark grey')
        pass_entry.configure(show='')
    else:
        hide_btn.configure(text_color='navy')
        pass_entry.configure(show='*')
def login():
    username = username_entry.get()
    password = pass_entry.get()

    if(username=="" or password==""):
        mb.showerror(title="Invalid credentials",message="Please Enter Correct credentials")
    else:
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='anish123',
            database='carnival'
        )

        mycursor = mydb.cursor()
        query = "select * from vol_login"
        mycursor.execute(query)
        row = mycursor.fetchall()
        print(row)
        for i in row:
            if(i[0] == username and i[1] == password):
                msg = 'yes'
                break
            else:
                msg = 'no'

        if(msg == 'yes'):
            mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='anish123',
            database='carnival'
            )
            mycursor = mydb.cursor()
            query2 = f"truncate current_vol"
            mycursor.execute(query2)
            query2 = f"insert into current_vol (vol_name) values ('{username}')"
            mycursor.execute(query2)
            # query3 = f"select * from current_vol"
            # mycursor.execute(query3)
            #print(mycursor.fetchall())
            mydb.commit()
            mb.showinfo(title="SUCCESS", message=f"LOGIN SUCCESSFULL, welcome '{username}'")
            window.destroy()
            import vol_homepage

        else:
            mb.showinfo(title="FAILED", message="LOGIN UNSUCCESSFULL")


frame = tr.Frame(bg='#fac6c6')

login_label = tr.Label(window,text='Volunteer Login',bg='#d1d5fd',font=("Times", 35))
username_label = ctk.CTkLabel(window,text='Username',bg_color='#d1d5fd',font=('Arial',18),text_color='#130c5b')
pass_label = ctk.CTkLabel(window,text='Password',bg_color='#d1d5fd',font=('Arial',18),text_color='#130c5b')
username_entry = ctk.CTkEntry(window,font=('Arial',15),width=150,height=26,fg_color='#d1d3e8',text_color='black')
pass_entry = ctk.CTkEntry(window,font=('Arial',15),width=150,height=26,fg_color='#d1d3e8',text_color='black',show='*')
login_btn = ctk.CTkButton(window,text='LOGIN',fg_color="#130c5b",corner_radius=50,width=90,command= login)
hide_btn = ctk.CTkButton(window,text='👁️',command=toggle_password,text_color='navy',hover_color='#c7cbf5',font=('Times',25),width=5,height=5,fg_color='#d1d5fd')
hide_btn.place(x=300,y=165)
reset_btn = ctk.CTkButton(window,text='RESET',fg_color="#130c5b",corner_radius=50,width=90,command=reset)
reset_btn.place(x=190,y=240)

login_label.place(x=50,y=10)
username_label.place(x=45,y=130)
pass_label.place(x=45,y=170)
username_entry.place(x= 150,y=130)
pass_entry.place(x=150,y=170)
login_btn.place(x=60,y=240)

frame.pack()


window.mainloop()




