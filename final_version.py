import tkinter.messagebox
from customtkinter import *
from tkinter.tix import Balloon
from PIL import ImageTk,Image
import sys

set_appearance_mode("System")  
set_default_color_theme("dark-blue")

w=CTk()
w.geometry('700x500')
w.title('Home')

logged_in = False
regist_in = False

password = ""
username = ""

pizza_prise = 0
pizza_num = 0
pizza_i_have = 0

gender = 0

google=ImageTk.PhotoImage(Image.open("google_l.png").resize((50,50), Image.LANCZOS))
instagram=ImageTk.PhotoImage(Image.open("Instagram_l.png").resize((50,50), Image.LANCZOS))

def new_func():
    f2=CTkFrame(w)
    f2.place(relx=0.5, rely=0.5, anchor=CENTER)
    img1=ImageTk.PhotoImage(Image.open("back.png").resize((3840,2160), Image.LANCZOS))
    l1=CTkLabel(master=f2,image=img1)
    l1.pack()

    
def default_home():
    new_func()
    l2=CTkLabel(w,text='Order a pizza', fg_color="#d94843", font=('Comic Sans MS',100))
    l2.place(relx=0.5, rely=0.5, anchor=CENTER)
   
def home():
    f1.destroy()
    new_func()
    l2=CTkLabel(w,text='Order a pizza',fg_color="#d94843",  font=('Comic Sans MS',65))
    l2.place(relx=0.5, rely=0.5, anchor=CENTER)
    toggle_win()
 

def pizza():
        f1.destroy()
        w.withdraw()
        pizza_main = CTkToplevel()
        pizza_main.geometry("700x500") 
        pizza_main.title("Size of pizza")

        img1=ImageTk.PhotoImage(Image.open("back_pizza.png").resize((3840,2160), Image.LANCZOS))
        label_pizza = CTkLabel(master=pizza_main, image=img1)
        label_pizza.pack()

        frame=CTkFrame(master=label_pizza, width=3840, height=2160, corner_radius=10, fg_color="white")
        frame.place(relx=0.5, rely=0.5, anchor=CENTER) 

        label = CTkLabel(master=frame,text='Choose a size', text_color="black", font=('Comic Sans MS',100)) 
        label.pack(pady=12,padx=10)

        def next(prise_size):
                pizza_main.destroy()

                global pizza_prise
                pizza_prise += prise_size

                def final(prise_toping):
                    pizza_top.destroy()
                    global pizza_prise
                    pizza_prise += prise_toping

                    def pizza_have():
                        pizza_f.destroy()
                        w.deiconify()
                        global pizza_num
                        pizza_num += 1
                        global pizza_prise
                        global pizza_i_have
                        pizza_i_have += pizza_prise
                        pizza_prise = 0

                        l2=CTkLabel(w,text="You have " + str(pizza_num) + " pizza!", fg_color="#d94843", font=('Comic Sans MS',65))
                        l2.place(relx=0.5, rely=0.5, anchor=CENTER)
                        toggle_win()

                    def pizza_not():
                        pizza_f.destroy()
                        w.deiconify()
                        global pizza_prise
                        pizza_prise = 0
                        if logged_in == False:
                            l1=CTkLabel(w,text="You didn't keep the pizza!\nPlease login first", fg_color="#d94843", font=('Comic Sans MS',50))
                            l1.place(relx=0.5, rely=0.5, anchor=CENTER)
                        elif pizza_num != 0:
                            l1=CTkLabel(w,text="You didn't keep the pizza!\nYou have " + str(pizza_num) + " pizza!", fg_color="#d94843", font=('Comic Sans MS',50))
                            l1.place(relx=0.5, rely=0.5, anchor=CENTER)
                        else:
                            l1=CTkLabel(w,text="You didn't keep the pizza!\nYou don't have pizza!", fg_color="#d94843", font=('Comic Sans MS',50))
                            l1.place(relx=0.5, rely=0.5, anchor=CENTER)
                        toggle_win()

                    pizza_f = CTkToplevel()
                    pizza_f.geometry("1000x500")
                    pizza_f.title('Your pizza')

                    img1=ImageTk.PhotoImage(Image.open("pizza_fin.png").resize((3840,2160), Image.LANCZOS))
                    label_fin = CTkLabel(pizza_f, image=img1)
                    label_fin.place(x=0, y=0, relwidth=1, relheight=1)

                    frame=CTkFrame(master=label_fin, width=3840, height=2160, corner_radius=10, fg_color="white")
                    frame.place(relx=0.5, rely=0.5, anchor=CENTER) 

                    label = CTkLabel(frame, text="Your pizza cost " + str(pizza_prise) + "LV", fg_color="white", text_color="black", font=('Comic Sans MS',100))
                    label.pack()

                    buttons_Final = CTkFrame(frame, fg_color="white")
                    buttons_Final.pack(pady = 5)

                    if logged_in == False:
                        pizza_not()

                    button1_final= CTkButton(master=buttons_Final, text="I want it", width=100, height=50, fg_color="white", text_color="black", hover_color='#AFAFAF', command=pizza_have)
                    button1_final.pack(side = LEFT, padx = 45)

                    button2_final= CTkButton(master=buttons_Final, text="I don't want it", width=100, height=50, fg_color="white", text_color="black",  hover_color='#AFAFAF', command=pizza_not)
                    button2_final.pack(side = LEFT, padx = 45)

                    pizza_f.mainloop()

                pizza_top = CTkToplevel() 
                pizza_top.geometry("1000x500")
                pizza_top.title('Toping of pizza')

                img1=ImageTk.PhotoImage(Image.open("back_pizza.png").resize((3840,2160), Image.LANCZOS))
                label_top = CTkLabel(pizza_top, image=img1)
                label_top.place(x=0, y=0, relwidth=1, relheight=1)

                frame=CTkFrame(master=label_top, width=3840, height=2160, corner_radius=10, fg_color="white")
                frame.place(relx=0.5, rely=0.5, anchor=CENTER) 

                label1 = CTkLabel(master=frame,text='Chose a toping', text_color="black", font=('Comic Sans MS',100), bg_color="white") 
                label1.pack(pady=12,padx=10)

                buttons_t = CTkFrame(frame, fg_color="white")
                buttons_t.pack(pady = 5)

                peperoni = ImageTk.PhotoImage(Image.open("peperoni.png").resize((500,350), Image.LANCZOS))
                kaprichoza = ImageTk.PhotoImage(Image.open("kaprichoza.png").resize((500,350), Image.LANCZOS))
                havai = ImageTk.PhotoImage(Image.open("havai.png").resize((500,350), Image.LANCZOS))

                button2= CTkButton(master=buttons_t, image=peperoni, text="", width=100, height=150, fg_color='white', hover_color='#AFAFAF', command=lambda: final(0))
                button2.pack(side = LEFT, padx = 45)
                        
                button3= CTkButton(master=buttons_t, image=kaprichoza, text="", width=100, height=150, fg_color='white',  hover_color='#AFAFAF', command=lambda: final(1))
                button3.pack(side = LEFT, padx = 45)

                button4= CTkButton(master=buttons_t, image=havai, text="", width=100, height=150, fg_color='white',  hover_color='#AFAFAF', command=lambda: final(2))
                button4.pack(side = LEFT, padx = 45)

                label_pr = CTkFrame(frame, fg_color="white")
                label_pr.pack(pady = 5)

                l1_t=CTkLabel(label_pr,text='Peperoni', text_color="black", font=('Comic Sans MS',50))
                l1_t.pack(side = LEFT , padx=50)

                l2_t=CTkLabel(label_pr,text='Kapricoza', text_color="black", font=('Comic Sans MS',50))
                l2_t.pack(side = LEFT , padx=50)

                l3_t=CTkLabel(label_pr,text='Hawai <3', text_color="black", font=('Comic Sans MS',50))
                l3_t.pack(side = LEFT , padx=50)

                label_plus = CTkFrame(frame, fg_color="white")
                label_plus.pack(pady = 5)

                l1_plus=CTkLabel(label_plus,text='+ 0 LV', text_color="black", font=('Comic Sans MS',50))
                l1_plus.pack(side = LEFT , padx=85)

                l2_plus=CTkLabel(label_plus,text='+ 1 LV', text_color="black", font=('Comic Sans MS',50))
                l2_plus.pack(side = LEFT , padx=85)

                l3_plus=CTkLabel(label_plus,text='+ 2 LV', text_color="black", font=('Comic Sans MS',50))
                l3_plus.pack(side = LEFT , padx=85)
                pizza_top.mainloop()
            
        buttons = CTkFrame(frame, fg_color="white")
        buttons.pack(pady = 5)

        reg_pizza = ImageTk.PhotoImage(Image.open("reg_pizza.png").resize((500,350), Image.LANCZOS))
        l_pizza = ImageTk.PhotoImage(Image.open("l_pizza.png").resize((500,350), Image.LANCZOS))
        xl_pizza = ImageTk.PhotoImage(Image.open("xl_pizza.png").resize((500,350), Image.LANCZOS))

        button2= CTkButton(master=buttons, image=reg_pizza, text="", width=100, height=150, fg_color='white', hover_color='#AFAFAF', command=lambda: next(9))
        button2.pack(side = LEFT, padx = 4)
                
        button3= CTkButton(master=buttons, image=l_pizza, text="", width=100, height=150, fg_color='white',  hover_color='#AFAFAF', command=lambda: next(12))
        button3.pack(side = LEFT, padx = 4)

        button4= CTkButton(master=buttons, image=xl_pizza, text="", width=100, height=150, fg_color='white',  hover_color='#AFAFAF', command=lambda: next(15))
        button4.pack(side = LEFT, padx = 4)

        label_pr = CTkFrame(frame, fg_color="white")
        label_pr.pack(pady = 5)

        l2=CTkLabel(label_pr,text='9 LV', text_color="black", font=('Comic Sans MS',50))
        l2.pack(side = LEFT ,pady = 5, padx=50)

        l2=CTkLabel(label_pr,text='12 LV', text_color="black", font=('Comic Sans MS',50))
        l2.pack(side = LEFT , padx=50)

        l2=CTkLabel(label_pr,text='15 LV', text_color="black", font=('Comic Sans MS',50))
        l2.pack(side = LEFT , padx=50)

        pizza_main.mainloop()

def cart():
        f1.destroy()
        new_func()
        global pizza_i_have
        global pizza_num

        def order():
            f1.destroy()
            new_func()

            l2=CTkLabel(w,text='Congrats !\nYou ordered a pizza',fg_color="#d94843",  font=('Comic Sans MS',65))
            l2.place(relx=0.5, rely=0.5, anchor=CENTER)

            global pizza_i_have
            global pizza_num
            global username

            class ParameterManager:
                def user(*args):
                    with open("order.txt", "w") as f:
                        f.write(f"Order: {' '.join(args)}\n")

            ParameterManager.user(username, str(pizza_i_have) + ' Lv', str(pizza_num) + " pizza")

            pizza_i_have = 0
            pizza_num = 0

            toggle_win()

        if logged_in == False:
            l2=CTkLabel(w,text="Please login first", fg_color="#d94843", font=('Comic Sans MS',35))
            l2.place(relx=0.5, rely=0.5, anchor=CENTER)
        elif pizza_num != 0:
            l2=CTkLabel(w,text="you have " + str(pizza_num) + " pizzas\nand this cost " + str(pizza_i_have) + "LV", fg_color="#d94843", font=('Comic Sans MS',35))
            l2.place(relx=0.5, rely=0.5, anchor=CENTER)
            b2 = CTkButton(w, text= "Order now!", text_color="black", fg_color="#d94843", hover_color="#b21807", font=('Comic Sans MS',35), command=order)
            b2.place(relx=0.5, rely=0.8, anchor=CENTER)
        else:
            l2=CTkLabel(w,text="you don't have pizzas", fg_color="#d94843", font=('Comic Sans MS',35))
            l2.place(relx=0.5, rely=0.5, anchor=CENTER)
        toggle_win()
   
def login():
    f1.destroy()  # Destroy the home page frame
    w.withdraw()  # Hide the main window
    global username
    global password
        
    # Define login function
    def validate_login():
        global username
        global password
        global logged_in
        logged_in = True

        if user_entry.get() == username and user_pass.get() == password:
            login_window.destroy()
            show_main_window()
            
        elif user_entry.get() == username and user_pass.get() != password:
            tkinter.messagebox.showwarning(title='Wrong password',message='Please check your password')

        elif user_entry.get() != username and user_pass.get() == password:
            tkinter.messagebox.showwarning(title='Wrong username',message='Please check your username')

        else:
            tkinter.messagebox.showerror(title="Login Failed",message="Invalid Username and password")

    def show_main_window():
        w.deiconify()
        new_func()
        l2 = CTkLabel(w, text='You are login!', fg_color="#d94843", font=('Comic Sans MS', 100))
        l2.place(relx=0.5, rely=0.5, anchor=CENTER)
        toggle_win()

    def forgot_pass():
        login_window.withdraw()
        app = CTkToplevel() 
        app.geometry("400x440")
        app.title('Forget password')

        img1=ImageTk.PhotoImage(Image.open("pattern.png").resize((3840,2160), Image.LANCZOS))
        label_bg = CTkLabel(master=app, image=img1)
        label_bg.pack()

        frame=CTkFrame(master=label_bg, width=3840, height=2160, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        label = CTkLabel(master=frame,text='New Password') 
        label.pack(pady=12,padx=10)

        def reset_password():
            
            new_password = entry1.get()
            confirm_password = entry2.get()

            if new_password == confirm_password:
                tkinter.messagebox.showinfo('Password Reset', 'Your password has been reset.')
                global password
                password = confirm_password
                app.destroy()
                login_window.deiconify()
            else:
                tkinter.messagebox.showerror('Password Reset Failed', 'The passwords do not match. Please try again.')

        global entry1
        entry1=CTkEntry(master=frame, width=220, placeholder_text='New Password', show="●")
        entry1.pack(pady=20,padx=10)
        global entry2
        entry2=CTkEntry(master=frame, width=220, placeholder_text='Confirm', show="●")
        entry2.pack(pady=20,padx=10)
        button1=CTkButton(master=frame, width=220, text="Continue", command=reset_password , corner_radius=6)
        button1.pack(pady=20,padx=10)
        app.mainloop()
    login_window = CTkToplevel() 
    login_window.geometry("400x400") 
    login_window.title("Login") 
    img1=ImageTk.PhotoImage(Image.open("back.png").resize((3840,2160), Image.LANCZOS))
    label = CTkLabel(master=login_window, image=img1)
    label.pack()

    frame=CTkFrame(master=label, width=3840, height=2160, corner_radius=10)
    frame.place(relx=0.5, rely=0.5, anchor=CENTER)    

    label_top =  CTkLabel(master=frame, text='Login', font=('Comic Sans MS',40), width=250)
    label_top.pack(pady=20,padx=10)

    user_entry = CTkEntry(master=frame, placeholder_text="Username", width=200)
    user_entry.pack(pady=12,padx=10) 

    user_pass = CTkEntry(master=frame, placeholder_text="Password", show="●", width=200)
    user_pass.pack(pady=12,padx=10)

    button_pass = CTkButton(master=frame, text='Forgot password', command=forgot_pass, width=200)
    button_pass.pack(pady=12,padx=10)

    button = CTkButton(master=frame, text='Login', command=validate_login, width=200)
    button.pack(pady=12,padx=10)

    checkbox = CTkCheckBox(master=frame, text='Remember Me')
    checkbox.pack(pady=12,padx=10)

    login_window.mainloop()


def logout():
    f1.destroy()
    new_func()
    global logged_in
    logged_in = False
    l2=CTkLabel(w,text='You are logout',fg_color="#d94843", font=('Comic Sans MS',50))
    l2.place(relx=0.5, rely=0.5, anchor=CENTER)
    toggle_win()

def exit():
    sys.exit(0)

def regist():
        f1.destroy() 
        w.withdraw()

        global logged_in
        logged_in = True

        def gender_callback(selected_val):
            global gender
            if selected_val == "Male":
                gender = 1
            elif selected_val == "Female":
                gender = 2
            elif selected_val == "I don't want to say":
                gender = 3
            elif selected_val == "Chose a gender":
                gender = 0

        def register_user():
            reg_window.withdraw()
            global username
            global password
            global gender 

            username = user_entry.get()
            password = user_pass.get()
            
            if username == "" and password == "":
                tkinter.messagebox.showerror(title="Registration Failed",message="You have not entered username and password")
                regist()

            elif password == "":
                tkinter.messagebox.showwarning(title='Wrong password',message='You have not entered password')
                regist()

            elif username == "":
                tkinter.messagebox.showwarning(title='Wrong username',message='You have not entered username')
                regist()

            elif gender == 0:
                tkinter.messagebox.showwarning(title="Gender Failed",message="Please enter gender")
                regist()
            else:
                tkinter.messagebox.showinfo(title='Successful',message='Successful registration!')
                global regist_in
                regist_in = True
                reg_window.destroy()
                show_regist_window()

        def show_regist_window():
            w.deiconify()  # Show the main window again
            new_func()
            l2 = CTkLabel(w, text="Welcome, " + username + "!", fg_color="#d94843", font=('Comic Sans MS', 65))
            l2.place(relx=0.5, rely=0.5, anchor=CENTER)
            toggle_win()


        reg_window = CTkToplevel()
        reg_window.geometry("400x350")
        reg_window.title("Registration")

        img1=ImageTk.PhotoImage(Image.open("back.png").resize((3840,2160), Image.LANCZOS))
        label = CTkLabel(master=reg_window, image=img1)
        label.pack()

        frame=CTkFrame(master=label, width=3840, height=2160, corner_radius=10)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)  

        label_top =  CTkLabel(master=frame, text='Regist', font=('Comic Sans MS',30), width=200)
        label_top.pack(pady=12,padx=10)

        user_entry = CTkEntry(master=frame,placeholder_text="Username") 
        user_entry.pack(pady=12,padx=10) 

        user_pass = CTkEntry(master=frame,placeholder_text="Password",show="●") 
        user_pass.pack(pady=12,padx=10)

        default_gender = "Chose a gender"

        gender_options = CTkOptionMenu(master=frame, values=["Male", "Female", "I don't want to say"], command=gender_callback)
        gender_options.pack(padx=10, pady=10)
        gender_options.set(default_gender)

        button = CTkButton(master=frame,text='Register',command=register_user) 
        button.pack(pady=12,padx=10)

        global google
        global instagram

        buttons = CTkFrame(frame)
        buttons.pack(pady = 12)
        
        button2= CTkButton(master=buttons, image=google, text="Google", width=100, height=20, fg_color='white', text_color='black', hover_color='#AFAFAF')
        button2.pack(side = LEFT, padx = 4)
        
        button3= CTkButton(master=buttons, image=instagram, text="Instagram", width=100, height=20, fg_color='white', text_color='black', hover_color='#AFAFAF')
        button3.pack()

        reg_window.mainloop()

def toggle_win():
    def dele():
        f1.destroy()
        b2=CTkButton(w, width= 10, height = 12, image=img1,
                     text="",
                     fg_color="white", 
                     corner_radius = 0,
               command=toggle_win,
               hover_color='#262626')
        b2.place(x=5,y=5)

    global f1
    f1=CTkFrame(w, width= 225, height=w.winfo_screenheight())
    f1.pack(side= LEFT)
    f1.configure(fg_color="#f9ca55")

    #buttons
    def bttn(padx,pady,text,cmd):
     

        myButton1 = CTkButton(f1,text=text,
                              text_color="black",
                       width=200,
                       fg_color="#f9ca55",
                       hover_color='#ffe56f',            
                       command=cmd,
                       font=('Comic Sans MS',14))
                      
        myButton1.pack(padx=padx,pady=pady)

    global img2
    img2=ImageTk.PhotoImage(Image.open("close.png").resize((100,100), Image.LANCZOS))
    
    CTkButton(w, width= 0, height = 0,
            text="",
           image=img2,
           fg_color="white", 
           hover_color='#262626',
           corner_radius= 3,
           command=dele,
           bg_color='#12c4c0').place(x=5,y=5)
    if regist_in == False:
        bttn(0,20,'H O M E',home)
        bttn(0,20, 'R E G I S T',regist)
        bttn(0,20, 'E X I T',exit)
    else:
        bttn(0,20,'H O M E',home)
        bttn(0,20,'P I Z Z A',pizza)
        bttn(0,20,'C A R T',cart)
        if logged_in == False:
            bttn(0,20,'L O G I N',login)
        else:
            bttn(0,20,'L O G O U T',logout)
            if gender == 1:
                image_gender = ImageTk.PhotoImage(Image.open("male.png").resize((100,100), Image.LANCZOS))
            elif gender == 2:
                image_gender = ImageTk.PhotoImage(Image.open("female.png").resize((100,100), Image.LANCZOS))
            else:
                image_gender = ImageTk.PhotoImage(Image.open("unknown.png").resize((100,100), Image.LANCZOS))

            def on_enter(event):
                l2.configure(text="Hello " + username + ", You are login!", bg_color="#f9ca55", text_color="black", font=('Comic Sans MS',15))

            def on_leave(event):
                l2.configure(text="")
            
            l2 = CTkLabel(w, text="")
            l2.place(x=5,y=55)

            gen = CTkButton(w,width= 10, height = 12,image=image_gender,
                        text="", 
                        fg_color="white",
                        bg_color="white",
                        command=None)
            gen.place(x=70,y=5)

            gen.bind("<Enter>", on_enter)
            gen.bind("<Leave>", on_leave)
        bttn(0,20, 'E X I T',exit)

default_home()

img1=ImageTk.PhotoImage(Image.open("open.png").resize((100,100), Image.LANCZOS))


b2=CTkButton(w,width= 10, height = 12,image=img1,
             text="",
             fg_color="white",
             hover_color='#262626',  
             corner_radius = 0,
       command=toggle_win)
b2.place(x=5,y=5)

w.mainloop()