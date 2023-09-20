import tkinter as tk
from tkinter import ttk as ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from main_logic import *
import time
import string
import sys

var1=0
var2=0
var3=0
var4=0
uname=''
class interface1:

    def __init__(self):
        self.root = tk.Tk()
        # self.root.title="Eyesolate"
        # self.root.iconbitmap("img\ubsafe.png")
        
        # self.root.iconbitmap("img/icon.ico")

        self.root.geometry("600x375")  # setting the interface size
        self.root.minsize(600, 375)

        self.root.maxsize(600, 375)
        self.root.title("UBSAFE")
        self.logo()
        self.text()
        self.root.configure()  # BLUE COLOR
        self.root.mainloop()

    def logo(self):
        self.image = Image.open("img/ubsafe.png")
        self.image = self.image.resize((250, 220), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.image)
        # changing the height width of the canvas
        self.canvas = tk.Canvas(self.root, width=200,height=160, highlightthickness=0)#background='#F0E68C'
        # defining the position of the image
        self.canvas.create_image(110, 100, image=self.photo)

        self.canvas.place(x=200, y=30)

    def text(self):
        # self.Ubsafe = tk.Label(self.root, text="UBSAFE", font=("Verdana", 28,), )  # Heading BLUE COLOR
        # self.Ubsafe.place(x=230, y=130)  # place of the Heading
        # self.open_progressbar()
        self.startButton = tk.Button(self.root, text="Start Applicaton", font=("ArialBlack", 18), fg="white", bg="red", command=lambda: self.load(self.startButton))
        self.startButton.place(x=210, y=300)
    
    def load(self, button):
        global var1
        var1 = 1
        if button.cget("text") == "Start Applicaton":
            button.destroy()
            if button.winfo_exists():
                print("problem")
            else:
                self.root.after(1000, self.open_progressbar)
    
    def open_progressbar(self):
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=500, mode="determinate") 
        self.progress.place(x=50, y=200)
        
        self.label = tk.Label(
            self.root, text="wait for the progress...",)
        self.label.place(x=200, y=230)
        self.progress["value"] = 0

        for i in range(11):
            self.label.config(text="You are %i%% there" %(self.progress["value"]), font=("Verdana", 12))
            self.root.update_idletasks()
            time.sleep(0.5)
            self.progress["value"] += 10
            # if i==3:
            #     self.label.destroy()
            # self.root.after(1000,self.check("Checking System Compatibility....",i))
            if i == 10:
                self.root.destroy()

class interface2:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("668x335")  # 385 # setting the interface size
        self.root.minsize(668, 335)
        self.root.maxsize(668, 335)

        self.root.title("EYESOLATE")
        # self.root.iconbitmap("logo\sbglogo.ico")
        # self.root.configure(bg="#F0E68C")
        self.heading()
        self.scroll()
        self.agree_and_next()
        self.root.mainloop()

    def heading(self):
        self.label = tk.Label(self.root, text="How To Use", font=("Verdana", 18))  # Color Khaki
        self.label.place(x=255, y=10)

    def scroll(self):
        self.text = tk.Text(self.root, width=70, height=17, font=("Verdana", 9, "bold"), wrap="word")
        self.text.place(x=15, y=50)
        self.text_value = """1. Enter the User Information such as Name, Phone Number, Gmail & Admin Gmail ID.

2. An interface will appear where User can select the 1 Touch Block SSH,USB & TOR or can enter custom scripts according to company policies.

3. After entering the custom script or 1 Touch Secure option  the System will send notification in the form of SMS and Gmail to user as well as admin.

4. If the client/user wants to add more security to his/her system, then the client can move to more settings options.

5. If the user tries to forcefully shutdown the application in between the complition of process then it software will not be liable of any security loosening.

--
"""

        self.text.insert(tk.END, self.text_value)
        self.text.tag_add("justify", "1.0", "end")
        self.text.tag_config("justify")
        self.scrollbar = tk.Scrollbar(self.root, bg="#00BFFF")
        self.scrollbar.pack(side="right", fill=tk.Y, pady=32)
        self.text.config(yscrollcommand=self.scrollbar.set)
        # self.root.configure("#00BFFF")
        self.scrollbar.config(command=self.text.yview)

    def agree_and_next(self):
        self.checkbtn_value = tk.IntVar()
        self.checkbtn = tk.Checkbutton(self.root, text="I agree to the terms & conditions..",variable=self.checkbtn_value, command=self.check_value)
        self.checkbtn.place(x=10, y=290)
        self.agree_btn = tk.Button(self.root, text="Next", command=self.exit_interface, fg="white", bg="Red", font=("Verdana", 10))

    def check_value(self):
        if self.checkbtn_value.get() == 1:
            self.agree_btn.place(x=606, y=300)

    def exit_interface(self):
        global var2
        var2=1
        self.root.destroy()

class interface3:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("560x455")  # width x height
        self.root.minsize(560, 455)
        self.root.maxsize(560, 455)

        self.root.title("UBSAFE")
        # self.root.iconbitmap("logo\sbglogo.ico")
        self.root.configure()
        self.var1 = self.var2 = self.var3 = 0
        self.form()
        # self.logo()
        self.submit()
        self.clear()
        self.root.mainloop()

    def form(self):
        # self.root.configure("#F0E68C")
        self.heading = tk.Label(self.root, text="System User Information", font=("Verdana", 18))  # COLOR KHAKI
        self.heading.place(x=150, y=10)

        self.name = tk.Label(self.root, text="User Name:",font=("Verdana", 14))  # name
        self.name.place(x=20, y=85)
        self.name_textbox = tk.Entry(self.root, width=35, font=("Verdana", 12))
        self.name_textbox.place(x=160, y=90)
        global uname
        # uname = self.name_textbox.get()
        
        # self.name1 = tk.Label(self.root,text=uname)
        # msg = "Mail System is working ," ; tmail = "abhiraj123sardar@gmail.com" ; p = uname
        # send_mail(msg,tmail,p)

        self.password=tk.Label(self.root,text="Password:",font=("Verdana", 14))
        self.password.place(x=20,y=140)
        self.password_textbox = tk.Entry(self.root, width=35, font=("Verdana", 12),show="*")
        self.password_textbox.place(x=160, y=145)

        #horizontal line
        separator = ttk.Separator(self.root, orient="horizontal")
        separator.pack(fill="x", padx=10, pady=185)

        self.emp_id=tk.Label(self.root,text="Employee Id:",font=("Verdana", 14))
        self.emp_id.place(x=20,y=200)
        self.emp_id_textbox = tk.Entry(self.root, width=35, font=("Verdana", 12))
        self.emp_id_textbox.place(x=160, y=206)

        #I need to update this part
        self.phone=tk.Label(self.root,text="Phone No:",font=("Verdana", 14))
        self.phone.place(x=20,y=240)
        self.phone_textbox = tk.Entry(self.root, width=35, font=("Verdana", 12))
        self.phone_textbox.place(x=160, y=246)

        self.uemail=tk.Label(self.root,text="Email:",font=("Verdana", 14))
        self.uemail.place(x=20,y=280)
        self.uemail_textbox = tk.Entry(self.root, width=35, font=("Verdana", 12))
        self.uemail_textbox.place(x=160, y=285)

        self.aemail=tk.Label(self.root,text="Admin Email:",font=("Verdana", 14))
        self.aemail.place(x=20,y=320)
        self.aemail_textbox = tk.Entry(self.root, width=35, font=("Verdana", 12))
        self.aemail_textbox.place(x=160, y=325)
    
    def clear(self):
        self.submit = tk.Button(self.root, text="  Clear  ", font=("Verdana", 14), fg="white", bg="Red",command=self.clear_data)
        self.submit.place(x=23, y=390)

    def clear_data(self):
        self.name_textbox.delete(0,tk.END)
        self.password_textbox.delete(0,tk.END)
        self.emp_id_textbox.delete(0,tk.END)
        self.phone_textbox.delete(0,tk.END)
        self.uemail_textbox.delete(0,tk.END)
        self.aemail_textbox.delete(0,tk.END)

    def submit(self):
        # self.submit_status=tk.IntVar()
        self.submit = tk.Button(self.root, text="Submit", font=("Verdana", 14), fg="white", bg="Red", command=self.getdata)
        self.submit.place(x=427, y=390)

# To fetch all inputed Data   
    def getdata(self):
        self.uname = self.name_textbox.get()
        self.passw = self.password_textbox.get()
        self.eid = self.emp_id_textbox.get()
        self.ph = self.phone_textbox.get()
        self.usremail = self.uemail_textbox.get()
        self.ademail = self.aemail_textbox.get()

# Printing the data value
        # print(self.uname)
        # print(self.passw)
        # print(self.eid)
        # print(self.emp_id)
        # print(self.ph)
        # print(self.usremail)
        # print(self.ademail)

        self.root.destroy()

    def submit_destroy(self):
        global var3
        var3=1
        self.root.destroy()

    # def delete(self):
    #     self.root.destroy()

class interface4:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("560x455")  # width x height
        self.root.title("UBSAFE")
        #self.root.iconbitmap("logo\sbglogo.ico")
        self.root.configure()
        self.heading()
        self.block_button()
        self.clear()
        self.more_settings()
        self.submit()
        self.root.mainloop()

    def heading(self):
        self.lb1=tk.Label(self.root,text="1 Touch Secure",font=("Verdana", 12))
        self.lb1.place(x=100,y=22)
        self.lb2=tk.Label(self.root,text="Custom Script",font=("Verdana", 12))
        self.lb2.place(x=360,y=22)
    
    def block_button(self):
        self.ssh=tk.Button(self.root,text="     Block SSH     ",font=("Verdana", 14),fg="white", bg="Red")
        self.ssh.place(x=70,y=90)
        self.ssh_textbox = tk.Entry(self.root, width=15 ,font=("Verdana", 18))
        self.ssh_textbox.place(x=300, y=95)

        self.tor=tk.Button(self.root,text="     Block TOR     ",font=("Verdana", 14),fg="white", bg="Red")
        self.tor.place(x=70,y=180)
        self.tor_textbox = tk.Entry(self.root, width=15 ,font=("Verdana", 18))
        self.tor_textbox.place(x=300, y=185)

        self.usb=tk.Button(self.root,text="     Block USB     ",font=("Verdana", 14),fg="white", bg="Red")
        self.usb.place(x=70,y=270)
        self.usb_textbox = tk.Entry(self.root, width=15 ,font=("Verdana", 18))
        self.usb_textbox.place(x=300, y=275)

    def clear(self):
        self.clear = tk.Button(self.root, text="  Clear  ", font=("Verdana", 14), fg="white", bg="green",command=self.clear_data)
        self.clear.place(x=23, y=390)

    def clear_data(self):
        self.ssh_textbox.delete(0,tk.END)
        self.tor_textbox.delete(0,tk.END)
        self.usb_textbox.delete(0,tk.END)

    def more_settings(self):
        self.settings = tk.Button(self.root, text="More Settings", font=("Verdana", 14), fg="white", bg="green")
        self.settings.place(x=210, y=390)
    
    def submit(self):
        # self.submit_status=tk.IntVar()
        self.submit = tk.Button(self.root, text="Submit", font=("Verdana", 14), fg="white", bg="green",command=self.submit_destroy)
        self.submit.place(x=440, y=390)
    
    def submit_destroy(self):
        self.root.destroy()

initial_page=interface1()
if var1==0:
    sys.exit(0)
else:
    how_to_use=interface2()
    if var2==0:
        sys.exit(0)
    else:
        user_information=interface3()
        if var3==0:
            sys.exit(0)
        else:
            blocking_page=interface4()