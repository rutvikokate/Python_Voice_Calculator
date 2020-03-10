import tkinter as tk
import tkinter.messagebox
from tkinter import *
import tkinter.font as font
import sys
impor
import math
import speech_recognition as sr  # import all libraries
import pyttsx3
import engineio
import time
from PIL import Image, ImageTk

root = Tk()
root.title("Calculator")
root.configure(background="white")
root.geometry("370x580+500+60")
root.maxsize(370,580)
root.minsize(370,580)

#Bottom Frame
bottomframe = Frame(root,bg='#002BFF', width=390,height=80)  
bottomframe.grid( row=8,columnspan=8)


#Label
'''logo=PhotoImage(file='logo.png')
Label1 = Label(root,foreground="black",background="white", font=("Bahnschrift", 14) ,width=180,image=logo)
Label1.grid(row=7, column=1,columnspan=2)'''
 

# Variables
equa = ""
equation = StringVar()
 
calculation = Label(root,textvariable = equation,foreground="#2A2A2A",font=("Bahnschrift", 24), width=21,height=2,bg='white')
#calculation.place(x=0, y=0, relwidth=1, relheight=1)
equation.set("Start calculating...")
calculation.grid(row=1, columnspan=8,pady=15)
global num



def btnPress(num):
    global equa
    equa = equa + str(num)
    equation.set(equa)
 
def EqualPress():
    global equa
    total = str(eval(equa))
    equation.set(total)
    equa = ""
 
def ClearPress():
    global equa
    equa = ""
    equation.set("")

def Back():
    global equa
    global num
    current_value = equation.get()
    equation.set(current_value[:-1])
    equa=current_value[:-1]
    

def Voice():
    engineio = pyttsx3.init()
    voices = engineio.getProperty('voices')
    engineio.setProperty('rate', 130)
    engineio.setProperty('voice', voices[0].id)
    def speak(text):
        engineio.say(text)
        engineio.runAndWait()
    engineio = pyttsx3.init()
    voices = engineio.getProperty('voices')

    


    r = sr.Recognizer()
    #r.energy_threshold = 4000
    mic = sr.Microphone()

    while 1:
        
        with mic as source:
            print('Listening...')
            text = 'Listening...'
            speak(text)

            audio = r.listen(source)
            #r.adjust_for_ambient_noise(source, duration=0.5)
            #r.dynamic_energy_threshold = True        # listen to the source
            try:
                # use recognizer to convert our audio into text part.
                text = r.recognize_google(audio)
                print("You said : {}".format(text))
            except:
                # In case of voice not recognized  clearly
                print("Sorry could not recognize your voice")
                speak("Could not understand")

        if text == 'exit':
            equation.set('Good Bye :D')
            root.update_idletasks()
            speak("Good Bye")
            break
            #sys.exit("Thankyou !")
        elif text == "clear":
            equation.set(" ")
        
            
            

        a = ''
        b = ''
        i = 0
        j = 0
        c = len(text)
        while text[j] != ' ':
            a = a+text[j]
            j = j+1
        j=j+1
        ch = text[j]
        if ch=='d':
            while text[j]!='y':
                j=j+1
            #j=j+1
        j=j+2
        while j != c:
            b = b+text[j]
            j = j+1
        
        a = float(a)
        b = float(b)
       
    
        ans=0
        if ch == '+':
            ans = a+b
            equation.set(ans)
            root.update_idletasks()
        
            
        elif ch == '-':
            ans = a-b
            equation.set(ans)
            root.update_idletasks()
        
        elif ch == 'x' or ch == 'X':
            ans = a*b
            equation.set(round(ans,2))
            root.update_idletasks()
            
        elif ch == '/' or ch=='d':
            if b!=0:
                ans = a/b
                equation.set(round(ans,2))
                root.update_idletasks()
            else:
                speak("Not defined")
                ans=0
                #equation.set(round(ans,2))
                root.update_idletasks()
        elif ch == '^':
            ans= math.pow(a,b)
            equation.set(ans)
            root.update_idletasks()
        else:
            ans = "Invalid Command"

        print(round(ans,2)) 
        equation.set(ans)
        speak("The answer is {}".format(round(ans,2)))
        #root.update_idletasks()
       



 #--------------------USER INTERFACE---------------------------#       


ok=PhotoImage(file='res/ok.png')
one=PhotoImage(file='res/one.png')
two=PhotoImage(file='res/two.png')
three=PhotoImage(file='res/three.png')
four=PhotoImage(file='res/four.png')
five=PhotoImage(file='res/five.png')
six=PhotoImage(file='res/six.png')
seven=PhotoImage(file='res/seven.png')
eight=PhotoImage(file='res/eight.png')
nine=PhotoImage(file='res/nine.png')
zero=PhotoImage(file='res/zero.png')
power=PhotoImage(file='res/power.png')
plus=PhotoImage(file='res/plus.png')
minus=PhotoImage(file='res/minus.png')
mul=PhotoImage(file='res/mul.png')
div=PhotoImage(file='res/div.png')
equal=PhotoImage(file='res/equal.png')
c=PhotoImage(file='res/c.png')
dot=PhotoImage(file='res/dot.png')
back=PhotoImage(file='res/back.png')


Button0 = Button(root, command = lambda:btnPress(0), border=0, relief=SOLID,width=70,bg='white',height=70,fg="white",font='Calibri',image=zero)
Button0.grid(row = 6, column = 2, padx=0, pady=2)
Button1 = Button(root, command = lambda:btnPress(1), border=0, relief=SOLID,width=70,bg='white',height=70,fg="white",font='Calibri',image=one)
Button1.grid(row = 3, column = 1, padx=0, pady=2)
Button2 = Button(root, command = lambda:btnPress(2), border=0, relief=SOLID,width=70,bg='white',height=70,fg="white",font='Calibri',image=two)
Button2.grid(row = 3, column = 2, padx=0, pady=2)
Button3 = Button(root, command = lambda:btnPress(3), border=0, relief=SOLID,width=70,bg='white',height=70,fg="white",font='Calibri',image=three)
Button3.grid(row = 3, column = 3, padx=0, pady=2)
Button4 = Button(root, command = lambda:btnPress(4), border=0, relief=SOLID,width=70,bg='white',height=70,fg="white",font='Calibri',image=four)
Button4.grid(row = 4, column = 1, padx=0, pady=2)
Button5 = Button(root, command = lambda:btnPress(5), border=0, relief=SOLID,width=70,bg='white',height=70,fg="white",font='Calibri',image=five)
Button5.grid(row = 4, column = 2, padx=0, pady=2)
Button6 = Button(root, command = lambda:btnPress(6), border=0, relief=SOLID,width=70,bg='white',height=70,fg="white",font='Calibri',image=six)
Button6.grid(row = 4, column = 3, padx=0, pady=2)
Button7 = Button(root, command = lambda:btnPress(7), border=0, relief=SOLID,width=70,bg='white',height=70,fg="white",font='Calibri',image=seven)
Button7.grid(row = 5, column = 1, padx=0, pady=2)
Button8 = Button(root, command = lambda:btnPress(8), border=0, relief=SOLID,width=70,bg='white',height=70,fg="white",font='Calibri',image=eight)
Button8.grid(row = 5, column = 2, padx=0, pady=2)
Button9 = Button(root, command = lambda:btnPress(9), border=0, relief=SOLID,width=70,height=70,fg="white",font='Calibri',image=nine,bg='white')
Button9.grid(row = 5, column = 3, padx=0, pady=2)
Plus = Button(root, text="+", command = lambda:btnPress("+"), border=0, relief=SOLID,width=70,height=70,font='Calibri',fg='white',image=plus,bg='white')
Plus.grid(row = 3, column = 4, padx=0, pady=2)
Minus = Button(root, text="-", command = lambda:btnPress("-"), border=0, relief=SOLID,width=70,height=70,font='Calibri',fg='white',image=minus,bg='white')
Minus.grid(row = 4, column = 4, padx=0, pady=2)
Multiply = Button(root, text="*", command = lambda:btnPress("*"), border=0, relief=SOLID,width=70,height=70,font='Calibri',fg='white',image=mul,bg='white')
Multiply.grid(row = 5, column = 4, padx=0, pady=2)
Divide = Button(root, text="/", command = lambda:btnPress("/"), border=0, relief=SOLID,width=70,height=70,font='Calibri',fg='white',image=div,bg='white')
Divide.grid(row = 6, column = 4, padx=0, pady=2)
Equal = Button(root, text="=", command = EqualPress, border=0, relief=SOLID,width=70,height=70,font='Calibri',fg='white',image=equal,bg='white')
Equal.grid(row=6, column=3, padx=0, pady=2)
Dot = Button(root, text=".", command = lambda:btnPress("."), border=0, relief=SOLID,width=70,height=70,font='Calibri',fg='white',image=dot,bg='white')
Dot.grid(row=7, column=3, padx=0, pady=(2,15))
Power= Button(root, text="^", command = lambda:btnPress("**"), border=0, relief=SOLID,width=70,height=70,font='Calibri',fg='white',image=power,bg='white')
Power.grid(row=7, column=4, padx=0, pady=(2,15))
Back = Button(root, text="C", command = Back, border=0, relief=SOLID,width=70,height=70,font='Calibri',fg='white',image=c,bg='white')
Back.grid(row = 6, column = 1, padx=0, pady=2)
Voice =Button(root, command = Voice,bd=0,relief=SOLID,width=180,height=50,fg='white',font=('Calibri',15),bg='#002BFF',image=ok,activebackground='#002BFF')
Voice.grid(row=8, column=2,columnspan=2)
Clear=Button(root, border=0,command=ClearPress, relief=SOLID,width=180,height=70,fg='white',font='Calibri',image=back,bg='white')
Clear.grid(row=7, column=1,columnspan=2,pady=(2,15))



root.mainloop()