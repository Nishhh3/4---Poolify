import customtkinter as ctk
import tkinter as tr
from tkinter import messagebox as mb
import mysql.connector
window = tr.Tk()
window.title("ENROLL")
window.geometry('1000x600')
window.configure(bg='#E9A5A5')
# window.resizable(False,False)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

desired_width = 1000
desired_height = 600
center_window(window, desired_width, desired_height)
ctk.CTkLabel(window,text="USER Registration",font=("Georgia",50,"italic","underline"),text_color="#6D0E33").place(x=290,y=10)
username_lb = ctk.CTkLabel(window,text="ENTER USERNAME          :",font=("Georgia",20,"bold"),text_color='#7F113C')
username_lb.place(x=150+100,y=150)
pass_lb = ctk.CTkLabel(window,text="ENTER PASSWORD          :",font=("Georgia",20,"bold"),text_color='#7F113C')
pass_lb.place(x=150+100,y=210)
cpass_lb = ctk.CTkLabel(window,text="CONFIRM PASSWORD    :",font=("Georgia",20,"bold"),text_color='#7F113C')
cpass_lb.place(x=150+100,y=270)

user_entry = ctk.CTkEntry(window,text_color="black",fg_color="#FFDDDE",font=("Times",20),width=210)
user_entry.place(x=450+100,y=150)
pass_entry = ctk.CTkEntry(window,text_color="black",fg_color="#FFDDDE",font=("Times",20),width=210)
pass_entry.place(x=450+100,y=210)
cpass_entry = ctk.CTkEntry(window,text_color="black",fg_color="#FFDDDE",font=("Times",20),width=210)
cpass_entry.place(x=450+100,y=270)
lb1 = ctk.CTkLabel(window,text=' ',fg_color='#E9A5A5',text_color='black',font=("calibri",20,'italic'))
lb1.place(x=760,y=150)
lb2 = ctk.CTkLabel(window,text=' ',fg_color='#E9A5A5',text_color='black',font=("calibri",20,'italic'))
lb2.place(x=760,y=210)
lb3 = ctk.CTkLabel(window,text=' ',fg_color='#E9A5A5',text_color='black',font=("calibri",20,'italic'))
lb3.place(x=760,y=270)
special_chars = ["!@#$%^&*()_+{}[]|\\:;<>,.?/~"]
sc = 'nspecial'
def clear():
    user_entry.delete(0,ctk.END)
    pass_entry.delete(0,ctk.END)
    cpass_entry.delete(0,ctk.END)

def register():
    sc = 'not special'
    if (user_entry.get() == '' or  pass_entry.get() == '' or  cpass_entry.get() == ''):
        mb.showerror(message="Please enter all fields !!")
    else:
        for char in user_entry.get():
            print(char)
            if char == '#' or char == '$' or char == '&' or char == ')' or char == '(' or char == '*' or char == '%' or char == '@' or char == '!' or char == '`' or char == '~':
                sc = 'special'
            else:
                sc = 'nspecial'
        print(sc)
        mydb = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='anish123',
            database='carnival'
        )

        mycursor = mydb.cursor()
        query = "select * from user_login"
        mycursor.execute(query)
        row = mycursor.fetchall()
        print(row)
        status = 'not exists'
        for i in row:
            if user_entry.get() in i:
                status = 'exists'
                break
            else:
                status = 'not exists'
        if sc == 'special':
            lb1.configure(text='*special char not allowed')
        elif status == 'exists':
            lb1.configure(text="*already exists")

        elif (len(pass_entry.get()) < 8):
            lb2.configure(text="*minimum 8 characters")
        elif (pass_entry.get() != cpass_entry.get()):
            lb3.configure(text='*passwords do not match')
        elif (status == 'not exists'):
            lb1.configure(text=' ')
            lb2.configure(text=' ')
            lb3.configure(text=' ')
            username = user_entry.get()
            password = pass_entry.get()
            values = [username, password]
            query = "INSERT INTO user_login (username, pass) VALUES (%s, %s)"
            mycursor.execute(query, values)
            mydb.commit()
            mydb.close()
            mb.showinfo(message="User registered Successfully !!!!!!!!!!")




reg_btn = ctk.CTkButton(window,text="REGISTER",font=("Georgia",18,"bold"),text_color='#7F113C',hover_color='silver',command=register,
                        border_width=3,corner_radius=100,fg_color='#D0B0B1',border_color='#7F113C')
reg_btn.place(x=555,y=340)
clr_btn = ctk.CTkButton(window,text="CLEAR",font=("Georgia",18,"bold"),text_color='#7F113C',hover_color='silver',command=clear,
                        border_width=3,corner_radius=100,fg_color='#D0B0B1',border_color='#7F113C')
clr_btn.place(x=330,y=340)


window.mainloop()