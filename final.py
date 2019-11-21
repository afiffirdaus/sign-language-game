import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
import sqlite3
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image
import random
import time
from tkinter import *
from threading import Thread
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2


    
class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        width  = self.winfo_screenwidth()
        height = self.winfo_screenheight()
        self.geometry(f'{width}x{height}')
       
                
        

        self.frames = {}
        for F in (LogIn, PageOne, PageTwo,PageThree,PageFour,PageScore,PDetails,PageUpdate,PageGame):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")
           
            self.show_frame("LogIn")
            
    def show_frame(self, page_name):
        global show_frame
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class LogIn(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        self.controller = controller
        
        global usern
        
        
        usern=tk.StringVar()
        passw=tk.StringVar()
        
        def Log():
            
            #Global variable
            global person1
            global dbscore
            
            while True:
                usernm=usern.get()
                passwrd=passw.get()
                with sqlite3.connect('Testing4.db') as db:
                    c = db.cursor()
                find_user=("Select*from User where Username=? AND Password=?")
                c.execute(find_user,[(usernm),(passwrd)])
                person1 = usernm
                results=c.fetchall()
                print(person1)
        
                if results: 
                   # for i in results:
                          messagebox.showinfo("Successful","Successfully Login")
                          
                          controller.show_frame("PageTwo")
                          
                          for row in results:
                              print("Username = ", row[0], )
                              print("Password = ", row[1])
                              print("Cpass  = ", row[2])
                              print("score  = ", row[3], "\n")
                              dbscore = row[3]
                              print(dbscore)
                          break
                else:
                    messagebox.showinfo("Fail","invalid username/password")
                    break
                
 
            
        label = tk.Label(self, text="Welcome to Sign School", font=("Times New Roman",35))
        label2 = tk.Label(self, text="Learn 5 vowel Letters",font=("Times New Roman",35))
        label.place(x=400, y=50)
        label2.place(x=420, y=120)
       
        
        label3 = tk.Label(self,text="Username",font=("Times New Roman",18))
        label3.place(x=450,y=350)
        
        label3 = tk.Label(self,text="Password",font=("Times New Roman",18))
        label3.place(x=450,y=400)
        
        
        e1=tk.Entry(self,textvar=usern)
        e1.place(x=650,y=360)
        
        e2=tk.Entry(self,textvar=passw,show="*")
        e2.place(x=650,y=405)
       # label3.pack(side="top", fill="x", pady=10)
        #entry1=Entry(self,StartPage)
        #entry1.place(x=450,y=360)
        tk.Button(self, text="Register",width=20,bg='brown',fg='white',
                            command=lambda: controller.show_frame("PageOne")).place(x=420,y=490)
        #tk.Button(self, text="Log In",width=20,bg='brown',fg='white',
         #                   command=lambda: controller.show_frame("PageTwo"),Log()).place(x=490,y=490)
        button2 = tk.Button(self, text="Login",width=20,bg='brown',fg='white',
                           command=lambda: [controller.show_frame("LogIn"),Log()]).place(x=700,y=490)
       # button1.pack()
       # button2.pack()



class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        Username=tk.StringVar()
        Password=tk.StringVar()
        Cpassword=tk.StringVar()
        Score=tk.StringVar()
        
        
            

        def database():
           name=Username.get()
           password=Password.get()
           cpassword=Cpassword.get()
           score=Score.get()
           
           conn = sqlite3.connect('Testing4.db')
           with conn:
               cursor=conn.cursor()
               cursor.execute('CREATE TABLE IF NOT EXISTS User (Username TEXT,Password TEXT,Cpassword TEXT,Score Int)')
               if len(password)<6:
                   messagebox.showinfo("Fail","Password at least 6 characters")
               elif Password.get() != Cpassword.get():
                   messagebox.showinfo("Fail","Password and Confirm password is inaccurate")
               else:    
                   cursor.execute('INSERT INTO User (Username,Password,Cpassword,Score) VALUES(?,?,?,?)',(name,password,cpassword,0))
                   conn.commit()
                   cursor.close()
                   messagebox.showinfo("Successful","Successfully Registered")
               
   
        label = tk.Label(self, text="Registration Form",font=("Times New Roman",35)).place(x=450,y=53)
        #label.pack(side="top", fill="x", pady=10)
        
        label_1 = tk.Label(self, text="Username",width=20,font=("bold", 15))
        label_1.place(x=400,y=180)
        
        
        entry_1 = tk.Entry(self,textvar=Username)
        entry_1.place(x=650,y=185)
        
        label_2 = tk.Label(self, text="Password",width=20,font=("bold", 15))
        label_2.place(x=400,y=240)
        
        entry2 = tk.Entry(self,textvar=Password)
        entry2.place(x=650,y=240)
        
        label_3 = tk.Label(self, text="Confirm Password",width=20,font=("bold", 15))
        label_3.place(x=365,y=300)
        
        entry_3 = tk.Entry(self,textvar=Cpassword)
        entry_3.place(x=650,y=300)
                
      
        
        button = tk.Button(self, text="Back",width=20,bg='brown',fg='white',
                           command=lambda: controller.show_frame("LogIn")).place(x=410,y=380)
        
        button2 = tk.Button(self, text="Submit",width=20,bg='brown',fg='white',
                           command=lambda: [controller.show_frame("LogIn"),database()]).place(x=700,y=380)
        
        
       


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
       
        label = tk.Label(self, text="Welcome to Sign School!",font=("Times New Roman",25)).place(x=450,y=0)
         
        #label.pack(side="top", fill="x", pady=10)
       
     #  label2=tk.Label(self, text=" ",font=("Times New Roman",20)).place(x=155,y=120)
        
               
        button3=tk.Button(self,text="Log Out",font=("Times New Roman",15),width=10,bg='brown',fg='white',command=lambda:controller.show_frame("LogIn") ).place(x=380,y=400)
        button=tk.Button(self,text="Personal Details",font=("Times New Roman",15),width=13,bg='brown',fg='white',command=lambda:controller.show_frame("PDetails") ).place(x=750,y=400)    
        button=tk.Button(self,text="Play",font=("Times New Roman",30),width=10,bg='brown',fg='white',command=lambda:controller.show_frame("PageThree") ).place(x=350,y=200)
        
        button2=tk.Button(self,text="Tutorial",font=("Times New Roman",30),width=10,bg='brown',fg='white',command=lambda:controller.show_frame("PageFour")).place(x=700,y=200)
        button2=tk.Button(self,text="Scoreboard",font=("Times New Roman",15),width=10,bg='brown',fg='white',command=lambda:controller.show_frame("PageScore")).place(x=570,y=400)
        
        
        
    
        

class PageThree(tk.Frame):
    
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Instructions!",font=("Times New Roman",25)).place(x=540,y=0)
        label = tk.Label(self, text="1.Put your hand in the green box displayed\n2. You are given 20 seconds to guess all the signs\n3. Every alphabet have a time limit for you to guess\n4. Once the time's up the game will stop immediately.\n5. Please press ESC to exit during game\n Good Luck!",font=("Times New Roman",20)).place(x=330,y=50)
        button=tk.Button(self,text="Back",font=("Times New Roman",20),width=10,bg='brown',fg='white',command=lambda:controller.show_frame("PageTwo") ).place(x=370,y=550)    
        button=tk.Button(self,text="Start",font=("Times New Roman",20),width=10,bg='brown',fg='white',command=lambda:controller.show_frame("PageGame") ).place(x=800,y=550)    
        
      
        
        
        
        
class PageFour(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        
        label = tk.Label(self, text="Instructions of the game!",font=("Comic Sans MS",35)).place(x=460,y=40)
        label2 = tk.Label(self, text="This is a sign language game that consist of 5 hand sign, A,E,I,O,U.\nFollow each and every picture's hand sign and learn!",font=("Comic Sans MS",15)).place(x=420,y=110)
        
        def ImgA():
            load=Image.open("A.png")
            render=ImageTk.PhotoImage(load)
            img = tk.Label(self, image=render)
            img.image = render
            img.place(x=560, y=200)
            
        
        def ImgE():
            load=Image.open("E.png")
            render=ImageTk.PhotoImage(load)
               
            img = tk.Label(self, image=render)
            img.image = render
            img.place(x=560, y=200)
            
        
        def ImgI():
            load=Image.open("I.png")
            render=ImageTk.PhotoImage(load)
               
            img = tk.Label(self, image=render)
            img.image = render
            img.place(x=560, y=200)
            
            
        def ImgO():
            load=Image.open("O.png")
            render=ImageTk.PhotoImage(load)
               
            img = tk.Label(self, image=render)
            img.image = render
            img.place(x=560, y=200)
            
            
        def ImgU():
            load=Image.open("U.png")
            render=ImageTk.PhotoImage(load)
               
            img = tk.Label(self, image=render)
            img.image = render
            img.place(x=560, y=200)
            
            
        button=tk.Button(self,text="A",font=("Times New Roman",20),width=10,bg='brown',fg='white',command=lambda:ImgA() ).place(x=100,y=100)
        button=tk.Button(self,text="E",font=("Times New Roman",20),width=10,bg='brown',fg='white',command=lambda:ImgE() ).place(x=100,y=200)
        button=tk.Button(self,text="I",font=("Times New Roman",20),width=10,bg='brown',fg='white',command=lambda:ImgI() ).place(x=100,y=300)
        button=tk.Button(self,text="O",font=("Times New Roman",20),width=10,bg='brown',fg='white',command=lambda:ImgO() ).place(x=100,y=400)
        button=tk.Button(self,text="U",font=("Times New Roman",20),width=10,bg='brown',fg='white',command=lambda:ImgU() ).place(x=100,y=500)
        button3=tk.Button(self,text="Back",font=("Times New Roman",20),width=10,bg='brown',fg='white',command=lambda:controller.show_frame("PageTwo") ).place(x=100,y=600)
        
        
        
        

        
    
       
class PageScore(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Scoreboard",font=("Comic Sans MS",35)).place(x=550,y=45)
       
        def Recent():
            conn=sqlite3.connect('Testing4.db')
            with conn:
                c=conn.cursor()
                
                c.execute("Select Username,Score From User ")
                conn.commit()
                result=c.fetchall()
                for index,dat in enumerate(result):
                    tk.Label(self, text=dat[0]).grid(row=index+1, column=0)
                    tk.Label(self, text=dat[1]).grid(row=index+1, column=1)
                   # tk.Label(self, text=dat[2]).grid(row=index+1, column=2)
                    
                    #label2.place(x=400,y=240)
               
                    
                c.close()
                
                #label=tk.Label(self, text=result,font=("Times New Roman",30)).place(x=200,y=120) 
        
          
        button=tk.Button(self,text="Back",font=("Times New Roman",20),width=10,bg='brown',fg='white',command=lambda:controller.show_frame("PageTwo") ).place(x=500,y=550)    
        button=tk.Button(self,text="View Recent",font=("Times New Roman",20),width=10,bg='brown',fg='white',command=lambda:Recent() ).place(x=700,y=550)    
        
class PDetails(tk.Frame):
    
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        def gen():
            global gen
            conn = sqlite3.connect('Testing4.db')
            with conn:
                c=conn.cursor()
                
                c.execute("select*from User where Username=(?)",(usern.get(),))
                conn.commit()
                result=c.fetchall()
                c.close()
                label = tk.Label(self, text=result,font=("Times New Roman",30)).place(x=150,y=120) 
                   
        def Deactivate():
                 conn = sqlite3.connect('Testing4.db')
                 with conn:
                     cursor=conn.cursor()
                     cursor.execute('delete from User where Username=(?)',(usern.get(),))
                     conn.commit()
                     messagebox.showinfo("Successful","Successfully Deactivated")
                     controller.show_frame("LogIn")    
        
        
                     
        
        label1 = tk.Label(self, text="Username",font=("Times New Roman",20)).place(x=100,y=60) 
        label2 = tk.Label(self, text="Password",font=("Times New Roman",20)).place(x=215,y=60) 
        label3 = tk.Label(self, text="Confirm Password",font=("Times New Roman",20)).place(x=330,y=60) 
        label4 = tk.Label(self, text="Score",font=("Times New Roman",20)).place(x=550,y=60)
        button4=tk.Button(self,text="",font=("Times New Roman",0),width=300,bg='brown',fg='white',command=lambda :gen()).place(x=0,y=0)    
        
        button1=tk.Button(self,text="Back",font=("Times New Roman",15),width=8,bg='brown',fg='white',command=lambda:controller.show_frame("PageTwo") ).place(x=70,y=250)    
        button2=tk.Button(self,text="Update",font=("Times New Roman",15),width=10,bg='brown',fg='white',command=lambda:controller.show_frame("PageUpdate") ).place(x=420,y=250)    
        button3=tk.Button(self,text="Deactivate Account",font=("Times New Roman",15),width=15,bg='brown',fg='white',command=lambda : Deactivate() ).place(x=580,y=250)
        button4=tk.Button(self,text="Generate details",font=("Times New Roman",15),width=15,bg='brown',fg='white',command=lambda :gen()).place(x=210,y=250)
        
        



class PageUpdate(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        
        
        label1 = tk.Label(self, text="Update User Details",font=("Times New Roman",20)).place(x=140,y=60) 
        
        olduser=tk.StringVar()
        newUser=tk.StringVar()
        newPass=tk.StringVar()
        newCPass=tk.StringVar()
        
        
        
        def UpdateUser():
           
            Nname=newUser.get()
            Npassword=newPass.get()
            Ncpassword=newCPass.get()
           
            conn = sqlite3.connect('Testing4.db')
            with conn:
               cursor=conn.cursor()
               
               if len(Npassword)<6:
                   messagebox.showinfo("Fail","Password at least 6 characters")
               elif newPass.get() != newCPass.get():
                   messagebox.showinfo("Fail","Password and Confirm password is inaccurate")
               else:
                   cursor.execute("Update User SET Username=?,Password=?,Cpassword=? WHERE Username=(?)",(Nname,Npassword,Ncpassword,usern.get(),))
                   conn.commit()
                   conn.close()
                   messagebox.showinfo("Successful","Successfully Updated")
                   controller.show_frame("LogIn") 
        
              
              
        button=tk.Button(self,text="Enter",font=("Times New Roman",15),width=15,bg='brown',fg='white',command=lambda :UpdateUser()).place(x=50,y=220)        
        button2=tk.Button(self,text="Back",font=("Times New Roman",15),width=15,bg='brown',fg='white',command=lambda:controller.show_frame("PDetails")).place(x=350,y=220)        
        
        
        
        label_4 = tk.Label(self, text="New Username",width=20,font=("bold", 15))
        label_4.place(x=80,y=130)
        
        entry_4 = tk.Entry(self,textvar=newUser)
        entry_4.place(x=350,y=130)
        
        label_2 = tk.Label(self, text="New Password",width=20,font=("bold", 15))
        label_2.place(x=80,y=160)
    
        entry_2 = tk.Entry(self,textvar=newPass)
        entry_2.place(x=350,y=160)
        
        label_3 = tk.Label(self, text="Re-Confirm password",width=20,font=("bold", 15))
        label_3.place(x=80,y=190)
        
        entry_3 = tk.Entry(self,textvar=newCPass)
        entry_3.place(x=350,y=190)


class PageGame(tk.Frame):
    
    def __init__(self, parent, controller):
        
        global person1
        global dbscore
        
        tk.Frame.__init__(self, parent)        
        #ipnut sume cam code 
        #ada timer, characters, score++ 
        #once timer habis dia akan revert use back to scorebaord and their final score
    
        #self.controller = controller
        
       # us=tk.StringVar()
       # pw=tk.StringVar()
      #  cp=tk.StringVar()
      #  sc=tk.StringVar()
        
                  
        def Game():
            import math
            import cv2
            import numpy as np
            
            
            
            cap = cv2.VideoCapture(0)
            
            print("Username is")
            print(person1)
            
            
            print("Score Dari DB ")
            print(dbscore)
            
            
     
            
            
           # nama=us.get()
          #  pasw=pw.get()
           # cpasw=cp.get()
          #  scr=sc.get()
            
            #print("ni value dalam variable")
            #print(usernm)
            #print(pasw)
            #print(cpasw)
           # print(scr)
            
            
            while(1):
               
                try:  #try is to catch error, if the small window did not capture any contour area
                              
                    ret, frame = cap.read()#ret will obtain value from getting the camera frame,either t or f and frame will get the next frame in the camera
                    
                    frame=cv2.flip(frame,1) #to flip vertically
                    kernel = np.ones((3,3),np.uint8)
                    
                    #state the specific box region it wanted to capture
                    box=frame[100:300, 100:300]
                    
                    
                    cv2.rectangle(frame,(100,100),(300,300),(0,255,0),0)    
                    hsv = cv2.cvtColor(box, cv2.COLOR_BGR2HSV)
   
                    
                    #bgr to HSV               
                     
                #the skin color in HSV
                    bottom_skin = np.array([0,20,70], dtype=np.uint8)
                    upper_skin = np.array([20,255,255], dtype=np.uint8)
                    
                    #mask skin color, if its 1,white which is hand else 0,back which is the mask 
                    mask = cv2.inRange(hsv, bottom_skin, upper_skin)
                    
               
                    
                    #extrapolate the hand to fill dark spots within
                    mask = cv2.dilate(mask,kernel,iterations = 4)
                    
                    #process of blurring the image, one type of blurring and smoothing,to reduce img noise
                    mask = cv2.GaussianBlur(mask,(5,5),100) 
                    
                    
                    
                    #outline shows in interest box
                    contours,hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
                
                    #find contour of the max area of palm
                    cntr = max(contours, key = lambda x: cv2.contourArea(x))
                    
                
                    epsilon = 0.0005*cv2.arcLength(cntr,True)
                    approx= cv2.approxPolyDP(cntr,epsilon,True)
                   
                    
                    #convex hull is made arnd palm, the green thing arnd palm
                    chull = cv2.convexHull(cntr)
                    
                    #state the area of hull and area of hand based on the top definations made
                    areahull = cv2.contourArea(chull)
                    areacnt = cv2.contourArea(cntr)
                  
                    #percentage not covered in chull
                    
                    arearatio=((areahull-areacnt)/areacnt)*100
                
                     #defects of chull compared to palm
                    chull = cv2.convexHull(approx, returnPoints=False)
                    defects = cv2.convexityDefects(approx, chull)
                    
                # l = no. of defects
                    l=0
                    
                #code to find defects due of fingers
                    for i in range(defects.shape[0]):
                        s,e,f,d = defects[i,0]
                        start = tuple(approx[s][0])
                        end = tuple(approx[e][0])
                        far = tuple(approx[f][0])
                        pt= (100,180)
                        
                        
                        # find length of all sides of triangle
                        a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                        b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                        c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                        s = (a+b+c)/2
                        ar = math.sqrt(s*(s-a)*(s-b)*(s-c))
                        
                        
                        d=(2*ar)/a
                        
                       
                        angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
                        
                    
                       
                        if angle <= 90 and d>30:
                            l += 1
                            cv2.circle(box, far, 3, [255,0,0], -1)
                        
                        
                        cv2.line(box,start, end, [0,255,0], 2)
                        
                        
                    l+=1
                    
 
                    
            
                    
                    score= dbscore
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    if l==1:
                        if areacnt<2000:
                            cv2.putText(frame,'Hand in the box!',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
        
                        else:
                            while arearatio<12:
                                cv2.putText(frame,'Correct A',(0,50), font, 2, (0,0,255), 3, cv2.LINE_AA)
                                score=score+1
                                a=a
                                print(score)
                                conn = sqlite3.connect('Testing4.db')
                                with conn:
                                   print("Jadi")
                                   cursor=conn.cursor()
                                   #cursor.execute('INSERT INTO User (Score) VALUES(10)')
                                   #cursor.execute('INSERT INTO User (Username,Password,Cpassword,Score) VALUES(?,?,?,?)',("a","aaaaaa","aaaaaa",score))
                                   cursor.execute("Update User SET Score=? WHERE Username=(?)",(score,person1))
                                   conn.commit()
                                   cursor.close()
                                #Thread(target = simpan(mark)).start()
                                break
                            
                            
                    #cv2.imshow('mask',mask)
                    cv2.imshow('frame',frame)
                except:
                    pass
                k = cv2.waitKey(5) & 0xFF
                if k == 27:
                    break
            
            cv2.destroyAllWindows()
            cap.release()
            
               
        def simpan(mark):
            conn = sqlite3.connect('Testing4.db')
            with conn:
                cursor=conn.cursor()
                jhg=aaaaaa
                print("Thread bejalan")
                print(mark)
                print("Correct A")
  #          insert_into_db=("INSERT INTO User (Username,Password,Cpassword,Score) VALUES(?,?,?,?)")
    #            cursor.execute('INSERT INTO User (Score) VALUES(?)',(mark))
                
                
                c.execute("Select Username,Score From User ")
                conn.commit()
                result=c.fetchall()
                for index,dat in enumerate(result):
                    print(text=dat[0])
                    tk.Label(self, text=dat[0]).grid(row=index+1, column=0)                                 
                c.close()
        
            
        def Countdown(t=1):
            global i
            i=1
            
            if(i==1):
                label = tk.Label(self, text="Timer:",font=("Times New Roman",25)).place(x=540,y=0)
                
                label = tk.Label(self, text=t,font=("Times New Roman",25)).place(x=700,y=0)
                
                if(t<=10):
                    self.after(1000,Countdown,t+1)
                   
                else:
                    i=1
                    label = tk.Label(self, text="Done",font=("Times New Roman",25)).place(x=540,y=0)
                    controller.show_frame("PageScore")
                    
        def Letter(t=10):
            global i
            global randd
            i=1
            
            if(i==1):
                label = tk.Label(self, text=t,font=("Times New Roman",25)).place(x=540,y=0)
                
                if(t>0):
                    self.after(5000,Letter,t-1)
            listofletters=['A','E','I','O','U'] 
                    
                    #self.after(1000,listofletters)
                     
            randd=random.choice(listofletters)
            label_3 = tk.Label(self, text=randd,width=5,font=("bold", 130))
            label_3.place(x=0,y=190)
                
        
        


        button=tk.Button(self,text="Lets Go!",font=("Times New Roman",15),width=15,bg='brown',fg='white',command=lambda :[Countdown(),Letter()]).place(x=500,y=500)
        button=tk.Button(self,text="Cam",font=("Times New Roman",15),width=15,bg='brown',fg='white',command=lambda :Thread(target = Game).start()).place(x=700,y=500)




if __name__ == "__main__":
    app = SampleApp()
#    app.mainloop()
    Thread(target = app.mainloop()).start()
    