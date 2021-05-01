# -*- coding: utf-8 -*-
#!usr/bin/python /home/pi/Desktop/asd.py

import Tkinter as tk
import RPi.GPIO as GPIO
import sys
import time
from firebase import firebase

GPIO.setmode(GPIO.BCM)
m1 = 7  #pwm단자
m2 =8   #pwm단자
ms = 20  #모션센서
pit1 = 6   #인터럽터
pit2 = 12 
pit3 = 16 
pit4 = 26 

GPIO.setwarnings(False)

#모터
GPIO.setup(m1, GPIO.OUT)
GPIO.setup(m2, GPIO.OUT)
GPIO.output (m1, False)
GPIO.output (m2, False)

p1 = GPIO.PWM(m1 , 400)
p2 = GPIO.PWM(m2 , 400)
#모션센서
GPIO.setup(ms, GPIO.IN)
#인터럽터
GPIO.setup(pit1, GPIO.IN)
GPIO.setup(pit2, GPIO.IN)
GPIO.setup(pit3, GPIO.IN)
GPIO.setup(pit4, GPIO.IN)


def stop():
      print('Motor STOP')
      p1.stop()
      p2.stop()
def pumping1():
        #파이어베이스에서 습도,기본값 등등 더해서 회전횟수 구하기
        p1.start(40)
        time.sleep(1.3)
        print('pumping')
        stop()

stop()
           
def r1():
        rotate1()
        addPage5()
def r2():
        rotate2()
        addPage2()
def r3():
        rotate3()
        addPage3()
def r4():
        rotate4()
        addPage4()


        
def rotate1():#1번화장품배출
        k=0
        l=3
        stop()
     
        while True:
            i = GPIO.input(pit1) #포토 인터럽터1
            j = GPIO.input(ms) #모션센서
        
            if i==0 :#배출구에 화장품이 위치안함
                  
                p2.start(15)
                print('Rotate')
            else: #배츌구에 화장품 옴
                print('1번화장품')
                
                i = GPIO.input(pit1)
                stop()
                j = GPIO.input(ms)
                
                if j==0:
                     time.sleep(0.1)
                     #insert()   #손이 감지가 안되면 대기
                     print('배출구 에 손을 넣어주세요')
                else: #손이감지되면 일정횟수 배출
                     while k<l:
                          k+=1
                          pumping1()
                     break
        stop()
def rotate2 ():#1번화장품배출
        k=0
        l=3
        stop()
     
        while True:
            i = GPIO.input(pit2) #포토 인터럽터2
            j = GPIO.input(ms) #모션센서
            if i==1 :#배출구에 화장품이 위치안함
                  
                p2.start(15)
                print('Rotate')
            else: #배츌구에 화장품 옴
                print('2번화장품')
                
                i = GPIO.input(pit1)
                stop()
                j = GPIO.input(ms)
                
                if j==1:
                     time.sleep(0.1)
                     #insert()   #손이 감지가 안되면 대기
                     print('배출구 에 손을 넣어주세요')
                else: #손이감지되면 일정횟수 배출
                     while k<l:
                          k+=1
                          pumping1()
                     break
                
        stop()
def rotate3():#3번화장품배출
        k=0
        l=3
        stop()
     
        while True:
            i = GPIO.input(pit3) #포토 인터럽터3
            j = GPIO.input(ms) #모션센서
            if i==1 :#배출구에 화장품이 위치안함
                  
                p2.start(15)
                print('Rotate')
            else: #배츌구에 화장품 옴
                print('3번화장품')
                
                i = GPIO.input(pit1)
                stop()
                j = GPIO.input(ms)
                
                if j==1:
                     time.sleep(0.1)
                     #insert()   #손이 감지가 안되면 대기
                     print('배출구 에 손을 넣어주세요')
                else: #손이감지되면 일정횟수 배출
                     while k<l:
                          k+=1
                          pumping1()
                     break
                
        stop()
def rotate4():#4번화장품배출
        k=0
        l=3
        stop()
     
        while True:
            i = GPIO.input(pit4) #포토 인터럽터4
            j = GPIO.input(ms) #모션센서
            if i==1 :#배출구에 화장품이 위치안함
                  
                p2.start(15)
                print('Rotate')
            else: #배츌구에 화장품 옴
                print('4번화장품')
                
                i = GPIO.input(pit1)
                stop()
                j = GPIO.input(ms)
                
                if j==1:
                     time.sleep(0.1)
                     #insert()   #손이 감지가 안되면 대기
                     print('배출구 에 손을 넣어주세요')
                else: #손이감지되면 일정횟수 배출
                     while k<l:
                          k+=1
                          pumping1()
                     break
                
        stop()



#추가배출 페이지
def addPage():
     addroot = tk.Toplevel()
     addroot.title("화장품 추가 배출")
     addroot.geometry("800x480")
     frame = tk.Frame(addroot,width=300)
     label = tk.Label(addroot,text='추가배출이 필요하신가요?',anchor='center',font='Times,40')
     label.pack()
     label.place(x='310',y='25')
     btn = tk.Button(addroot,text='예',command=pumping1,height='16',width='18',bd='0',bg='orange')
     btn.pack()
     btn.place(x='175',y='100')
     btn2 = tk.Button(addroot,text='아니오',height='16',width='18',bd='0',bg='orange')
     btn2.bind('<Button-1>',lambda e:addbr(addroot))
     btn2.pack()
     btn2.place(x='475',y='100')
     addroot.mainloop()
def addbr(addroot):
      addroot.destroy()
      r2()
def addPage2():
     addroot2 = tk.Toplevel()
     addroot2.title("화장품 추가 배출")
     addroot2.geometry("800x480")
     frame3 = tk.Frame(addroot2,width=300)
     label3 = tk.Label(addroot2,text='추가배출이 필요하신가요?',anchor='center',font='Times,40')
     label3.pack()
     label3.place(x='310',y='25')
     btn9 = tk.Button(addroot2,text='예',command=pumping1,height='16',width='18',bd='0',bg='orange')
     btn9.pack()
     btn9.place(x='175',y='100')
     btn10 = tk.Button(addroot2,text='아니오',height='16',width='18',bd='0',bg='orange',command=addbr2)
     btn10.bind('<Button-1>',lambda e:addbr2(addroot2))
     btn10.pack()
     btn10.place(x='475',y='100')
     addroot2.mainloop()
def addbr2(addroot2):
      addroot2.destroy()
      r3()
def addPage3():
     addroot3 = tk.Toplevel()
     addroot3.title("화장품 추가 배출")
     addroot3.geometry("800x480")
     frame2 = tk.Frame(addroot3,width=300)
     label2 = tk.Label(addroot3,text='추가배출이 필요하신가요?',anchor='center',font='Times,40')
     label2.pack()
     label2.place(x='310',y='25')
     btn7 = tk.Button(addroot3,text='예',command=pumping1,height='16',width='18',bd='0',bg='orange')
     btn7.pack()
     btn7.place(x='175',y='100')
     btn8 = tk.Button(addroot3,text='아니오',height='16',width='18',bd='0',bg='orange')
     btn8.bind('<Button-1>',lambda e:addbr3(addroot3))
     btn8.pack()
     btn8.place(x='475',y='100')
     addroot3.mainloop()
def addbr3(addroot3):
      addroot3.destroy()
      r4()
def add4Page():
     addroot4 = tk.Toplevel()
     addroot4.title("화장품 추가 배출")
     addroot4.geometry("800x480")
     frame2 = tk.Frame(addroot4,width=300)
     label2 = tk.Label(addroot4,text='추가배출이 필요하신가요?',anchor='center',font='Times,40')
     label2.pack()
     label2.place(x='310',y='25')
     btn7 = tk.Button(addroot4,text='예',command=pumping1,height='16',width='18',bd='0',bg='orange')
     btn7.pack()
     btn7.place(x='175',y='100')
     btn8 = tk.Button(addroot4,text='아니오',height='16',width='18',bd='0',bg='orange')
     btn8.bind('<Button-1>',lambda e:addbr4(addroot4))
     btn8.pack()
     btn8.place(x='475',y='100')
     addroot4.mainloop()
def addbr4(addroot4):
      addroot4.destroy()

def addPage5():
     addroot5 = tk.Toplevel()
     addroot5.title("화장품 추가 배출")
     addroot5.geometry("800x480")
     frame2 = tk.Frame(addroot5,width=300)
     label2 = tk.Label(addroot5,text='추가배출이 필요하신가요?',anchor='center',font=('Times'))
     label2.pack()
     label2.place(x='310',y='25')
     btn7 = tk.Button(addroot5,text='예',command=pumping1,height='16',width='18',bd='0',bg='orange')
     btn7.pack()
     btn7.place(x='175',y='100')
     btn8 = tk.Button(addroot5,text='아니오',height='16',width='18',bd='0',bg='orange')
     btn8.bind('<Button-1>',lambda e:addbr5(addroot5))
     btn8.pack()
     btn8.place(x='475',y='100')
     addroot5.mainloop()
def addbr5(addroot5):
      addroot5.destroy()

#옵션페이지
def genSub():
    oproot = tk.Toplevel()
    myGUI=Option(oproot)
    

class Option():
      
      def __init__(self,master):
     
           self.cos1 = firebase.get('/cosmatic','cosmatic1')
           self.cos2 = firebase.get('/cosmatic','cosmatic2')
           self.cos3 = firebase.get('/cosmatic','cosmatic3')
           self.cos4 = firebase.get('/cosmatic','cosmatic4')
           
           self.master = master
           self.master.geometry('800x480')
           self.master.title('Option')
           self.im = tk.PhotoImage(file="back.gif")
           self.c=tk.Canvas(self.master, width='800', height='480')
           self.c.pack()
           self.c.create_image(400,240,image=im)

           self.label1 = tk.Label(self.master,text='화장품 배출량',anchor='center',bg='white', font=('verdana',15))
           self.label1.pack()
           self.label1.place(x='140',y='30')

           self.label5 = tk.Label(self.master,text='잔량',anchor='center',bg='white', font=('verdana',12))
           self.label5.pack()
           self.label5.place(x='310',y='375')

           self.w1= tk.Scale(self.master, label='화장품1', fg='blue',bg='white', highlightbackground='white',troughcolor='skyblue',length=150,
                from_=1, to_=10, orient='horizontal', font=('verdana',12))
           self.w1.set(1)
           self.w1.pack()
           self.w1.place(x='140',y='75')

           self.w2= tk.Scale(self.master, label='화장품2', fg='blue',bg='white', highlightbackground='white',troughcolor='skyblue',length=150,
                from_=1, to_=10, orient='horizontal', font=('verdana',12))
           self.w2.set(self.cos2)
           self.w2.pack()
           self.w2.place(x='140',y='150')

           self.w3= tk.Scale(self.master, label='화장품3', fg='blue',bg='white', highlightbackground='white',troughcolor='skyblue',length=150,
                from_=1, to_=10, orient='horizontal', font=('verdana',12))
           self.w3.set(self.cos3)
           self.w3.pack()
           self.w3.place(x='140',y='225')

           self.w4= tk.Scale(self.master, label='화장품4', fg='blue',bg='white', highlightbackground='white',troughcolor='skyblue',length=150,
                from_=1, to_=10, orient='horizontal', font=('verdana',12))
           self.w4.set(self.cos4)
           self.w4.pack()
           self.w4.place(x='140',y='300')
     
           self.btn1 = tk.Button(self.master,text='저 장',bd='0',bg='orange')
           self.btn1.place(x='600',y='350')
           self.btn1.bind('<Button-1>',lambda e:save()) 

           self.btn2 = tk.Button(self.master,text='닫 기',bd='0',bg='orange',command=self.master.destroy)

           self.btn2.place(x='715',y='350')
     


           oproot.mainloop()

def save(self):
    cos1=w1.self.w1.get()
    cos2=self.w2.get()
    cos3=self.w3.get()
    cos4=self.w4.get()
    
    resultput = firebase.put('/cosmetic1','cosmetic1',cos1)
    resultput2 = firebase.put('/cosmetic2','cosmetic2',cos2)
    resultput3 = firebase.put('/cosmetic3','cosmetic3',cos3)
    resultput4 = firebase.put('/cosmetic4','cosmetic4',cos4)
   
    self.master.destroy()



#mainPage
firebase = firebase.FirebaseApplication("https://dytitan02.firebaseio.com/",None)

root = tk.Tk()
root.geometry("800x480")
frame1 = tk.Frame(root)
im = tk.PhotoImage(file="back.gif")
c=tk.Canvas(root, width='800', height='480')
c.pack()
c.create_image(400,240,image=im)
화장품 잔여량
photo1 = tk.PhotoImage(file="cos1.gif")
photo2 = tk.PhotoImage(file="cos2.gif")
photo3 = tk.PhotoImage(file="cos3.gif")
photo4 = tk.PhotoImage(file="cos4.gif")
photo5 = tk.PhotoImage(file="auto.gif")
photo6 = tk.PhotoImage(file="opt.gif")

btn = tk.Button(root,text='화장품1',command=r1,height='218',width='60',bd='0',image=photo1)
btn.place(x='285',y='0')

btn2 = tk.Button(root,text='화장품2',command=r2,height='213',width='60',bd='0',image=photo2)
btn2.place(x='450',y='0')

btn3 = tk.Button(root,text='화장품3',command=r3,height='214',width='68',bd='0',image=photo3)
btn3.place(x='285',y='250')

btn4 = tk.Button(root,text='화장품4',command=r4,height='245',width='60',bd='0',image=photo4)
btn4.place(x='450',y='240')

btn5 = tk.Button(root,text='AUTO',command=r1,height='100',width='74',bd='0',image=photo5)
btn5.place(x='365',y='187')

btn6 = tk.Button(root,text='option',command=optionPage,height='67',width='67',bd='0',image=photo6)
btn6.place(x='700',y='40')

label = tk.Label(root,text='AUTO',anchor='center',font='Times,60')
label.pack()
label.place(x='385',y='300')



     

root.mainloop()

